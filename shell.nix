let
  pkgs = import <nixpkgs> {};
in
 pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.numpy
      python-pkgs.pandas
      python-pkgs.matplotlib
    ]))
  ] ++ [pkgs.pyright];

  # Workaround: make vscode's python extension read the .venv
  shellHook = ''
    venv="$(cd $(dirname $(which python)); cd ..; pwd)"
    ln -Tsf "$venv" .venv
  '';
}  
