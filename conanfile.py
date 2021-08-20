from conans import ConanFile, CMake

class DlfcnWin32(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   name = "dlfcn-win32"
   generators = "cmake"
   version = "v1.3.0"

   def source(self):
      self.run("git clone https://github.com/dlfcn-win32/dlfcn-win32.git")

   def imports(self):
      self.copy("*.dll", dst="bin", src="bin") # From bin to bin
      self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin

   def build(self):
      cmake = CMake(self)
      cmake.configure(source_folder="dlfcn-win32")
      cmake.build()