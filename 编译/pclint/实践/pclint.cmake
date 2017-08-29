# This file contains functions and configurations for generating PC-Lint build
# targets for your CMake projects.

set(PCLINT_EXECUTABLE "${SCRIPTS_DIR}/check/lint/pclint/lint-nt.exe" CACHE STRING "full path to the pc-lint executable. NOT the generated lin.bat")
set(PCLINT_BAT "${SCRIPTS_DIR}/check/lint/pclint/lint-nt.bat" CACHE STRING "full path to the pc-lint bat.")
set(PCLINT_CONFIG_DIR "${SCRIPTS_DIR}/check/lint/pclint" CACHE STRING "full path to the directory containing pc-lint configuration files")
set(PCLINT_USER_FLAGS "-b" CACHE STRING "additional pc-lint command line options -- some flags of pc-lint cannot be set in option files (most notably -b)")

set(PCLINT_CACHE_DIR $ENV{TMP}/_lint_cache CACHE STRING "pclint acche dir")
file(MAKE_DIRECTORY ${PCLINT_CACHE_DIR})

# a phony target which causes all available *_LINT targets to be executed
add_custom_target(ALL_PCLINT)

# add_pclint(target source1 [source2 ...])
#
# Takes a list of source files and generates a build target which can be used
# for linting all files
#
# The generated lint commands assume that a top-level config file named
# 'std.lnt' resides in the configuration directory 'PCLINT_CONFIG_DIR'. This
# config file must include all other config files. This is standard lint
# behaviour.
#
# Parameters:
#  - target: the name of the target to which the sources belong. You will get a
#            new build target named ${target}_LINT
#  - source1 ... : a list of source files to be linted. Just pass the same list
#            as you passed for add_executable or add_library. Everything except
#            C and CPP files (*.c, *.cpp, *.cxx) will be filtered out.
#
# Example:
#  If you have a CMakeLists.txt which generates an executable like this:
#
#    set(MAIN_SOURCES main.c foo.c bar.c)
#    add_executable(main ${MAIN_SOURCES})
#
#  include this file
#
#    include(/path/to/pclint.cmake)
#
#  and add a line to generate the main_LINT target
#
#   if(COMMAND add_pclint)
#    add_pclint(main ${MAIN_SOURCES})
#   endif(COMMAND add_pclint)
#

function(add_pclint target)
    get_directory_property(lint_include_directories INCLUDE_DIRECTORIES)
    get_directory_property(lint_defines COMPILE_DEFINITIONS)

    # let's get those elephants across the alps
    # prepend each include directory with "-i"; also quotes the directory
    set(lint_include_directories_transformed 
        -i"${SCRIPTS_DIR}/check/lint/pclint/gcc4.1.2/x86_64-pc-linux-gnu/include" 
        -i"${SCRIPTS_DIR}/check/lint/pclint/gcc4.1.2/x86_64-pc-linux-gnu/lib/include"
        -i"${SCRIPTS_DIR}/check/lint/pclint/gcc4.1.2/include/c++/4.1.2"
        -i"${SCRIPTS_DIR}/check/lint/pclint/gcc4.1.2/include/c++/4.1.2/x86_64-pc-linux-gnu")

    foreach(include_dir ${lint_include_directories})
        list(APPEND lint_include_directories_transformed -i"${include_dir}")
    endforeach(include_dir)

    # 通过lnt文件传入头文件目录
    set(include_lnt "${CMAKE_CURRENT_BINARY_DIR}/${target}.include.lnt")
    file(WRITE ${include_lnt} "\n")
    foreach(include_dir ${lint_include_directories_transformed})
        file(APPEND ${include_lnt} "${include_dir}\n")
    endforeach(include_dir)

    # prepend each definition with "-d"
    set(lint_defines_transformed)
    foreach(definition ${lint_defines})
        list(APPEND lint_defines_transformed -d${definition})
    endforeach(definition)
        
    # list of all commands, one for each given source file
    set(outlint ${CMAKE_CURRENT_BINARY_DIR}/${target}_PCLINT.txt)
    set(pclint_commands)
    list(APPEND pclint_commands ${PCLINT_EXECUTABLE} -V > ${outlint})

    foreach(sourcefile ${ARGN})
        # only include c and cpp files
        if( sourcefile MATCHES \\.c$|\\.cc$|\\.cxx$|\\.cpp$ )
            # make filename absolute
            get_filename_component(srcfile ${sourcefile} ABSOLUTE)
            get_filename_component(srcfile_name ${sourcefile} NAME)
            set(outfile ${PCLINT_CACHE_DIR}/${srcfile_name}.${target}.LINT)
            set(include_d ${CMAKE_CURRENT_BINARY_DIR}/${srcfile_name}.d)

            # 支持增量PCLINT
            string(REPLACE "/" "\\" srcfile ${srcfile})
            string(REPLACE "/" "\\" outfile ${outfile})
            string(REPLACE "/" "\\" outlint ${outlint})
            list(APPEND pclint_commands COMMAND ${PCLINT_BAT}
                ${include_lnt}
                ${include_d}
                ${srcfile}
                ${outfile})
        endif()
    endforeach(sourcefile)
    
    #合并结果文件
    string(REPLACE "/" "\\" srclint ${PCLINT_CACHE_DIR}/*.${target}.LINT)
    list(APPEND pclint_commands COMMAND COPY /Y 
        ${srclint}
        ${outlint}
        > nul)

    # add a custom target consisting of all the commands generated above
    add_custom_target(${target}_PCLINT ${pclint_commands} VERBATIM)
    # make the ALL_LINT target depend on each and every *_LINT target
    add_dependencies(ALL_PCLINT ${target}_PCLINT)
endfunction(add_pclint)

