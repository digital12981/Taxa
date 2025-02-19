{pkgs}: {
  deps = [
    pkgs.pango
    pkgs.harfbuzz
    pkgs.glib
    pkgs.ghostscript
    pkgs.fontconfig
    pkgs.libev
    pkgs.postgresql
    pkgs.openssl
  ];
}
