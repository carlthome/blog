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
    hash = "";
  };


  propagatedBuildInputs = with python3Packages; [
    nltk
  ];

  meta = {
    description = "Python implementation of the Rapid Automatic Keyword Extraction algorithm using NLTK";
    homepage = "https://github.com/csurfer/rake-nltk";
    license = lib.licenses.mit;
  };
}
