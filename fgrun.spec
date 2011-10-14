Summary:	Graphical launcher for the FlightGear flight simulator
Name:		fgrun
Version:	1.6.0
Release:	%mkrel 1
Source0:	http://prdownloads.sourceforge.net/fgrun/%{name}-%{version}.tar.bz2
License:	GPLv2
Group:		Games/Other
URL:		http://sourceforge.net/projects/fgrun/
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	fltk-devel >= 1.1.0
BuildRequires:	imagemagick
BuildRequires:	cmake
BuildRequires:	simgear-devel >= 2.4.0
BuildRequires:	openscenegraph-devel >= 3.0.0
Requires:	flightgear >= 2.4.0

%description
fgrun is a graphical launcher for the FlightGear flight simulator.

%prep
%setup -q

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%__mkdir_p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment= Graphical launcher for the FlightGear flight simulator
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;Simulation;
EOF

%__mkdir_p %{buildroot}%{_miconsdir}
%__mkdir_p %{buildroot}%{_liconsdir}
convert -size 16x16 flightgear.png %{buildroot}%{_miconsdir}/%{name}.png
convert -size 48x48 flightgear.png %{buildroot}%{_liconsdir}/%{name}.png
%__install -m 644 flightgear.png %{buildroot}%{_iconsdir}/%{name}.png

%files -f %{name}.lang
%doc README COPYING NEWS AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png

