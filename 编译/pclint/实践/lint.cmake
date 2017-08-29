#PCLINT检查
option(PCLINT "pc_lint check only" OFF)
if(PCLINT)
    include(${SCRIPTS_DIR}/check/lint/pclint/pclint.cmake)
endif(PCLINT)

#STLINT检查
option(STLINT "st_lint check only" OFF)
if(STLINT)
    include(${SCRIPTS_DIR}/check/lint/stlint/stlint.cmake)
endif(STLINT)

function(add_lint target)
    if(PCLINT)
        add_pclint(${target} ${ARGN})
    elseif(STLINT)
        add_stlint(${target} ${ARGN})
    endif()
endfunction(add_lint)

