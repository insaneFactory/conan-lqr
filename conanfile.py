from conans import ConanFile, CMake, tools


class LqrConan(ConanFile):
	name = "lqr"
	version = "0.4.2"
	license = "LGPL-3.0"
	description = "Liquid Rescale library"
	settings = "os", "compiler", "build_type", "arch"
	generators = "cmake"
	requires = "glib/2.58.1@insanefactory/stable"
	exports = "CMakeLists.txt"
	options = {
		"shared": [True, False]
	}
	default_options = {
		"shared": True
	}

	def configure(self):
		del self.settings.compiler.libcxx

	def source(self):
		self.run("git clone https://github.com/carlobaldassi/liblqr.git src")
		self.run("cd src && git checkout v" + self.version)

	def build(self):
		cmake = CMake(self)
		cmake.configure(defs={
			"shared": self.options.shared
		})
		cmake.build()

	def package(self):
		self.copy("*.h", dst="include", src="src/lqr")
		self.copy("*.lib", dst="lib", keep_path=False)
		self.copy("*.dll", dst="bin", keep_path=False)
		self.copy("*.so", dst="lib", keep_path=False)
		self.copy("*.dylib", dst="lib", keep_path=False)
		self.copy("*.a", dst="lib", keep_path=False)

	def package_info(self):
		self.cpp_info.libs = ["lqr"]
