Summary:	Graphical launcher for the FlightGear flight simulator
Name:		fgrun
Version:	3.4.0
Release:	3
License:	GPLv2+
Group:		Games/Other
Url:		http://sourceforge.net/projects/fgrun/
Source0:	https://github.com/FlightGear/fgrun/archive/version/%{name}-version-%{version}-final.tar.gz
Source1:	flightgear.png
Patch0:		fgrun-1.6.1-fedora-fix-crash-when-setting-defaults.patch
Patch1:		fgrun-1.6.2-default-settings-for-rosa.patch
Patch2:		0004-Fix-reloadPath-logic.patch
Patch5:		fgrun-1.7.0-fedora-build-fgrun-with-static-ui-libs.patch
BuildRequires:	cmake
BuildRequires:	imagemagick
BuildRequires:	boost-devel
BuildRequires:	fltk-devel >= 1.3.0
BuildRequires:	simgear-devel
BuildRequires:	pkgconfig(openscenegraph)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xinerama)
Requires:	flightgear

%description
fgrun is a graphical launcher for the FlightGear flight simulator.

%files -f %{name}.lang
%doc README COPYING NEWS AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_sysconfdir}/fltk/flightgear.org/fgrun.prefs

#----------------------------------------------------------------------------

%prep
%setup -q -n fgrun-version-%{version}-final
%autopatch -p1

%build
#cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release
%cmake
%make

%install
%makeinstall_std -C build

mkdir -p %{buildroot}%{_sysconfdir}/fltk/flightgear.org
install -m 0644 fgrun.prefs \
	%{buildroot}%{_sysconfdir}/fltk/flightgear.org/fgrun.prefs

%find_lang %{name}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Graphical launcher for the FlightGear flight simulator
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;Simulation;
EOF

mkdir -p %{buildroot}%{_miconsdir}
mkdir -p %{buildroot}%{_liconsdir}
convert -size 16x16 %{SOURCE1} %{buildroot}%{_miconsdir}/%{name}.png
convert -size 48x48 %{SOURCE1} %{buildroot}%{_liconsdir}/%{name}.png
install -m 644 %{SOURCE1} %{buildroot}%{_iconsdir}/%{name}.png

