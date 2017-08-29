CMAKE_FLAGS := -DPCLINT:bool=ON -DLINT:bool=ON

all: rcp

rcp: deps cmake
	@cd build && mingw32-make.exe ALL_PCLINT

cmake:
	@cd build && cmake $(CMAKE_FLAGS) ..\..\..\..\..\ -G"MinGW Makefiles" 

deps:
	@IF NOT EXIST build MKDIR build

clean: 
	@IF EXIST build RMDIR /S /Q build

clean_cache:
	@IF EXIST $(TMP)\_lint_cache RMDIR /Q /S $(TMP)\_lint_cache
