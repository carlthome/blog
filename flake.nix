{
  description = "Nikola blog development environment";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }: flake-utils.lib.eachDefaultSystem (system:
    let pkgs = nixpkgs.legacyPackages.${system};
    in {
      packages.rake-nltk = pkgs.callPackage ./rake_nltk.nix { };

      packages.pythonEnv = pkgs.python3.withPackages (ps: with ps; [
        nikola
        nltk
        tqdm
        kaggle
        ipywidgets
        jq
        self.packages.${system}.rake-nltk
      ]);

      packages.default = pkgs.stdenv.mkDerivation {
        name = "blog";
        src = ./.;
        buildInputs = [
          self.packages.${system}.pythonEnv
        ];
      };

      apps.default =
        let
          app = pkgs.writeShellApplication {
            name = "blog";
            runtimeInputs = [ self.packages.${system}.pythonEnv ];
            text = ''
              nikola serve
            '';
          };
        in
        {
          type = "app";
          program = "${app}/bin/blog";
        };

      devShells.default = (pkgs.mkShell {
        name = "nikola";
        packages = builtins.attrValues self.packages.${system};
      });
    });
}
