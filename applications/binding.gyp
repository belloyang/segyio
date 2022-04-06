{
  "targets": [
    {
      "target_name": "segyinfo",
      "cflags!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags_cc!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags": ["-Wall", "-Wextra", "-Wpedantic"],
      "cflags_cc": ["-Wall", "-Wextra", "-Wpedantic"],
      "type": "executable",
      "sources": [
        "segyinfo.c"
      ],
     
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      },
      "xcode_settings": {
        "GCC_ENABLE_CPP_EXCEPTIONS" : "YES",
      },
      "include_dirs" :  [
          ".",
          "../lib/src",
          "../lib/include"
      ],
      'dependencies': [
          '../lib/binding.gyp:libsegyio',
      ]
      
    },
    {
      "target_name": "segyinspect",
      "cflags!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags_cc!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags": ["-Wall", "-Wextra", "-Wpedantic"],
      "cflags_cc": ["-Wall", "-Wextra", "-Wpedantic"],
      "type": "executable",
      "sources": [
        "segyinspect.c",
      ],
     
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      },
      "xcode_settings": {
        "GCC_ENABLE_CPP_EXCEPTIONS" : "YES",
      },
      "include_dirs" :  [
          ".",
          "../lib/src",
          "../lib/include"
      ],
      'dependencies': [
          '../lib/binding.gyp:libsegyio',
      ]
      
    },
    {
      "target_name": "segyio-catb",
      "cflags!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags_cc!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags": ["-Wall", "-Wextra", "-Wpedantic"],
      "cflags_cc": ["-Wall", "-Wextra", "-Wpedantic"],
      "type": "executable",
      "sources": [
        "apputils.c",
        "segyio-catb.c",
      ],
     
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      },
      "xcode_settings": {
        "GCC_ENABLE_CPP_EXCEPTIONS" : "YES",
      },
	  "defines": ["segyio_MINOR", "segyio_MAJOR"],
      "include_dirs" :  [
          ".",
          "../lib/src",
          "../lib/include"
      ],
      'dependencies': [
          '../lib/binding.gyp:libsegyio',
      ]
      
    },
    {
      "target_name": "segyio-cath",
      "cflags!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags_cc!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags": ["-Wall", "-Wextra", "-Wpedantic"],
      "cflags_cc": ["-Wall", "-Wextra", "-Wpedantic"],
      "type": "executable",
      "sources": [
        "segyio-cath.c",
      ],
     
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      },
      "xcode_settings": {
        "GCC_ENABLE_CPP_EXCEPTIONS" : "YES",
      },
	  "defines": ["segyio_MINOR", "segyio_MAJOR"],
      "include_dirs" :  [
          ".",
          "../lib/src",
          "../lib/include"
      ],
      'dependencies': [
          '../lib/binding.gyp:libsegyio',
      ]
      
    },
    {
      "target_name": "segyio-catr",
      "cflags!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags_cc!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags": ["-Wall", "-Wextra", "-Wpedantic"],
      "cflags_cc": ["-Wall", "-Wextra", "-Wpedantic"],
      "type": "executable",
      "sources": [
        "segyio-catr.c",
      ],
     
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      },
      "xcode_settings": {
        "GCC_ENABLE_CPP_EXCEPTIONS" : "YES",
      },
      "defines": ["segyio_MINOR", "segyio_MAJOR"],
      "include_dirs" :  [
          ".",
          "../lib/src",
          "../lib/include"
      ],
      'dependencies': [
          '../lib/binding.gyp:libsegyio',
      ]
      
    },
    {
      "target_name": "segyio-crop",
      "cflags!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags_cc!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags": ["-Wall", "-Wextra", "-Wpedantic"],
      "cflags_cc": ["-Wall", "-Wextra", "-Wpedantic"],
      "type": "executable",
      "sources": [
        "segyio-crop.c",
      ],
     
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      },
      "xcode_settings": {
        "GCC_ENABLE_CPP_EXCEPTIONS" : "YES",
      },
      "defines": ["segyio_MINOR", "segyio_MAJOR"],
      "include_dirs" :  [
          ".",
          "../lib/src",
          "../lib/include"
      ],
      'dependencies': [
          '../lib/binding.gyp:libsegyio',
      ]
      
    },
    {
      "target_name": "flip-endianness",
      "cflags!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags_cc!": ["-fno-exceptions", "-Wno-unused-parameter"],
      "cflags": ["-Wall", "-Wextra", "-Wpedantic"],
      "cflags_cc": ["-Wall", "-Wextra", "-Wpedantic"],
      "type": "executable",
      "sources": [
        "flip-endianness.cpp",
      ],
     
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      },
      "xcode_settings": {
        "GCC_ENABLE_CPP_EXCEPTIONS" : "YES",
      },
      "defines": ["segyio_MINOR", "segyio_MAJOR"],
      "include_dirs" :  [
          ".",
          "../lib/src",
          "../lib/include"
      ],
      'dependencies': [
          '../lib/binding.gyp:libsegyio',
      ]
      
    }
  ] 
}
