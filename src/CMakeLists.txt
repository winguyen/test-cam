add_executable(test-cam)

target_sources(test-cam PRIVATE
    main.cpp
)

include_directories( 
    ${OpenCV_INCLUDE_DIRS}
)

target_link_libraries(test-cam PRIVATE
    ${OpenCV_LIBS}
)

install(TARGETS test-cam RUNTIME)
