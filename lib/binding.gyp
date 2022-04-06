{
  "targets": [
    {
      "target_name": "segyio",
      "cflags!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags_cc!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags": ["-Wall", "-Wextra", "-Wpedantic"],
      "cflags_cc": ["-Wall", "-Wextra", "-Wpedantic"],
      "type": "shared_library",
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
