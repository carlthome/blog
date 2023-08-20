{ pkgs
, lib
, fetchPypi
, python3Packages
}:
pkgs.python3Packages.buildPythonPackage {
  name = "rake-nltk";
  format = "setuptools";

  src = fetchPypi {
    pname = "rake-nltk";
    version = "1.0.6";
    hash = "sha256-eBPWgLLOd7Uc2sF1f4Aah/9HaCydvSmCrqO2ZzA0YSI=";
  };

  propagatedBuildInputs = with python3Packages; [
    nltk
  ];

  pythonImportsCheck = [
    "rake_nltk"
  ];

  meta = {
    description = "Python implementation of the Rapid Automatic Keyword Extraction algorithm using NLTK";
    homepage = "https://github.com/csurfer/rake-nltk";
    license = lib.licenses.mit;
  };
}
