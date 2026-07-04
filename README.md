# straw
Cross-distro package management unified wrapper for Fedora, Ubuntu/Debian, Arch, openSUSE, and Atomic variants (Silverblue / Kinoite / Bazzite / Bluefin / Aurora).

## Features
- **Typo auto-correction**: `intall` → `install`, `serach` → `search`, `remve` → `remove`, etc.
- **Cross-distro pkg name mapping**: `libssl-dev` ↔ `openssl-devel`, `build-essential` ↔ `base-devel`, etc.
- **Flatpak subcommands**: `flat-install`, `flat-remove`, `flat-upgrade`, `flat-repair`
- **Atomic / OSTree support**: Bazzite app → Flatpak auto-redirect, OSTree whitelist (`vulkan-devel`, `gamemode`, `mangohud`, `nvidia-driver`, etc.)
- **Major release upgrade**: `straw sysupgrade` (Fedora `system-upgrade`, Ubuntu `do-release-upgrade`, Debian manual steps)
- **i18n**: `zh_CN` / `zh_TW` / `en_US`
- **Zero runtime deps**: Single-file bash script, only requires the distro's native package manager.

## Support Status
### ✅ Fedora / Atomic variants (Silverblue, Kinoite, Bazzite, Bluefin, Aurora)
Best support, covers ostree, Flatpak redirection, and sysupgrade. Main testing environment.

### ⚠️ Ubuntu / Debian
Basic `install`/`remove`/`search` works, `sysupgrade` (`do-release-upgrade`) available. Package name map entries are gradually being added.

### ⚠️ Arch (pacman) / openSUSE (zypper)
Backend hooked up, basic `install`/`remove`/`search` works. `sysupgrade` and full package mapping not yet ready.

### 🚧 Alpine (apk) / Void (xbps)
Backend stub only. Currently throws error: `"Alpine Linux $(_ status_dev)"` (same for Void). Implementation pending.
## How to install
You can install Straw manually or via Copr (Fedora/Alma/RHEL).
### ✅ manual install
1.Download the latest release asset (a file called "straw")into your download folder  
2.go to your download folder,and open it in Terminal
3.Enter:  
`chmod + x straw`  
`sudo mv straw /usr/local/bin/`
### ✅ copr install (ONLY FOR FEDORA/ALMA/RHEL)
`sudo dnf copr enable haoahohi/Straw`  
`sudo dnf install straw`
