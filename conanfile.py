from conan import ConanFile
from conan.errors import ConanException
from conan.tools.cmake import CMakeToolchain, CMakeDeps, cmake_layout, CMake

import os

class Conan(ConanFile):
    settings = "build_type"

    # def requirements(self):
        # self.requires("opencv/4.12.0")

    def layout(self):
        cmake_layout(self)
        self.folders.build = os.path.join("build", str(self.settings.build_type))
        self.folders.generators = os.path.join(self.folders.build, "generators")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

        # os.environ["GTEST_COLOR"] = "1"
        # cmake.ctest(cli_args=["--output-on-failure", "--timeout 30", "--schedule-random"])

    def package(self):
        cmake = CMake(self)
        cmake.install()
        
