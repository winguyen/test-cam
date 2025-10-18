add_executable(test-cam)

target_sources(test-cam PRIVATE
    main.cpp
)

target_link_libraries(test-cam PRIVATE
    libcamera
)

install(TARGETS test-cam RUNTIME)