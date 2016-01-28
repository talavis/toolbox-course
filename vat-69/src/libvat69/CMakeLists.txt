set(libsources barrel.f90 bottle.f90 brew.f90 brew.c)

if(MAKE_SHARED)
	add_library(libvat69 SHARED ${libsources})
else()
	add_library(libvat69 STATIC ${libsources})
endif()

install(TARGETS libvat69 DESTINATION lib)
