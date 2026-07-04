Name:           straw
Version:        2.4.0
Release:        1%{?dist}
Summary:        Cross-distro package management unified tool
License:        GPL-3.0-or-later
Source0:        %{name}-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  bash, coreutils
# 真正硬依赖（脚本运行时）
Requires:       bash, sudo

# —— 按发行版后端拆 Suggests，装 straw 的机器不会被强拉别的包管理器 ——

# Fedora/RHEL/CentOS 系后端
Suggests:       (dnf5 >= 5 or dnf >= 4 or yum)
# Ubuntu/Debian 系（用户跑 apt 系发行版时才有用）
Suggests:       apt
# Arch
Suggests:       pacman
# openSUSE
Suggests:       zypper

# Flatpak 子命令
Suggests:       flatpak
# sysupgrade_fedora → get_latest_fedora 需要
Suggests:       curl, jq

%description
straw is a cross-distro package manager wrapper for Fedora, Ubuntu/Debian,
Arch, openSUSE, and Atomic variants (Silverblue/Kinoite/Bazzite/Bluefin/Aurora).

Features:
- Typo auto-correction (intall → install, serach → search, etc.)
- Cross-distro pkg name mapping (libssl-dev ↔ openssl-devel, build-essential ↔ base-devel, etc.)
- Flatpak subcommands (flat-install, flat-remove, flat-upgrade, flat-repair)
- Atomic/OSTree support with Bazzite app → Flatpak auto-redirect
- OSTree whitelist (vulkan-devel, gamemode, mangohud, nvidia-driver, etc.)
- Major release upgrade helpers (Fedora via system-upgrade, Ubuntu do-release-upgrade, Debian manual steps)
- i18n: zh_CN / zh_TW / en_US

%prep
%setup -q

%install
# 主命令：/usr/bin/straw
install -Dpm 0755 straw %{buildroot}%{_bindir}/straw

# 兼容别名：老用户继续敲 `str`
ln -sf %{_bindir}/straw %{buildroot}%{_bindir}/str

%files
%license LICENSE
%{_bindir}/straw
%{_bindir}/str

%changelog
* Wed Jul 04 2026
- Fixed the issue of running twice when installing a wrong package with DNF on Fedora Linux (01)
- Fixed other bugs (02)
