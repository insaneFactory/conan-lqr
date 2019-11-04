from conans import ConanFile, CMake, tools
import os


class LqrConan(ConanFile):
	name = "lqr"
	version = "0.4.2"
	license = "LGPL-3.0"
	description = "Liquid Rescale library"
	settings = "os", "compiler", "build_type", "arch"
	generators = "cmake"
	build_requires = "cmake_installer/3.15.5@conan/stable"
	requires = "glib/2.58.3@bincrafters/stable"
	exports = "CMakeLists.txt"
	options = {
		"shared": [True, False]
	}
	default_options = {
		"shared": True
	}
	_source_subfolder = "source_subfolder"

	def configure(self):
		del self.settings.compiler.libcxx

	def source(self):
		archive = "liblqr-%s" % self.version
		tools.get("https://github.com/carlobaldassi/liblqr/archive/v%s.tar.gz" % self.version)
		os.rename(archive, self._source_subfolder)
		
	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

	def package(self):
		self.copy("*.h", dst="include/lqr", src=os.path.join(self._source_subfolder, "lqr"))
		self.copy("*.lib", dst="lib", keep_path=False)
		self.copy("*.dll", dst="bin", keep_path=False)
		self.copy("*.so", dst="lib", keep_path=False)
		self.copy("*.dylib", dst="lib", keep_path=False)
		self.copy("*.a", dst="lib", keep_path=False)

	def package_info(self):
		self.cpp_info.libs = ["lqr"]
		self.cpp_info.includedirs = [
			"include/lqr",
			"include"
		]
