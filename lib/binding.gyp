{
  "targets": [
    {
      "target_name": "libsegyio",
      "cflags!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags_cc!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags": ["-Wall", "-Wextra", "-Wpedantic", "-std=c99"],
      "cflags_cc": ["-Wall", "-Wextra", "-Wpedantic"],
      "type": "static_library",
      "sources": [
        "src/segy.c"
      ],
     
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      },
      "xcode_settings": {
        "GCC_ENABLE_CPP_EXCEPTIONS" : "YES",
      },
	  "defines": ["HAVE_SYS_STAT_H"],
      "include_dirs" :  [
          "src/",
          "include/"
      ]
      
    }
  ] 
}
