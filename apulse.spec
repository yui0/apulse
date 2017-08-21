%define name apulse
%define version 0.1.10
%define release b1

Name:		%{name}
Summary:	PulseAudio emulation for ALSA
Version:	%{version}
Release:	%{release}
License:	MIT
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}
Provides:	pulseaudio-libs
BuildRequires:	glib2-devel

%description
PulseAudio emulation for ALSA.

%prep
%setup -q

%build
cmake -DAPULSEPATH=%{buildroot}/%{_libdir} -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr -DCMAKE_BUILD_TYPE=Release .
make

%install
make install

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%files
%defattr (-,root,root)
/usr/bin/apulse
%{_libdir}/*

%changelog
* Mon Mar 13 2017 Yuichiro Nakada <berry@berry-lab.net>
- Create for Berry Linux
