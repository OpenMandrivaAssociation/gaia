%define name gaia
%define version 0.1.2
%define release %mkrel 5

Summary: Open 3D earth viewer with GPS support
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: gaia-0.1.2-fixgps.patch
License: GPL
Group: Sciences/Other
Url: https://sourceforge.net/projects/gaia-clean/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: scons
BuildRequires: SDL-devel
BuildRequires: curl-devel
BuildRequires: gpsd-devel
BuildRequires: jpeg-devel
BuildRequires: mesaglu-devel
BuildRequires: png-devel

%description
Gaia is an open 3D earth viewer with GPS support.

%prep
%setup -q
%patch0 -p1 -b .fixgps

%build
scons prefix=%{_prefix} gpsd=1

%install
rm -rf %{buildroot}
# (blino) scons install prefix=%{buildroot}%{_prefix} will recompile with a wrong datadir
install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}
install -D data/font.png %{buildroot}%{_datadir}/%{name}/font.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/font.png


