%define libname %mklibname presage 0
%define devname %mklibname -d presage
%define beta beta20150909

Name:		presage
Summary:	Predictive text entry system library
Version:	0.9.2
Release:	%{?beta:0.%{beta}.}2
Url:		https://presage.sourceforge.io/
Source0:	https://master.dl.sourceforge.net/project/presage/presage/%{version}~beta/presage-%{version}~%{beta}.tar.gz
Patch0:		presage-0.9.2-compile.patch
Patch1:		presage-0.9.2-no-underlinking.patch
Patch2:		https://sourceforge.net/p/presage/patches/3/attachment/0001-Add-missing-ONLINE_LEARNING-configuration-value-to-d.patch
Patch3:		https://sourceforge.net/p/presage/patches/2/attachment/fix-apostrophes.patch
License:	GPLv2
BuildRequires:	pkgconfig(python3)
BuildRequires:	python
BuildRequires:	help2man
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	swig
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(xevie)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gdk-x11-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	tinyxml-devel
BuildRequires:	python-dbus
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	desktop-file-utils
BuildRequires:	boost-algorithm-devel
BuildRequires:	boost-range-devel
BuildRequires:	boost-mpl-devel
Group:		System/Libraries

%description
Predictive text entry system library

%package -n %{libname}
Summary:	Predictive text entry system library
Group:		System/Libraries

%description -n %{libname}
Predictive text entry system library

%package -n %{devname}
Summary:	Development files for the predictive text entry system library
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for the predictive text entry system library

%package -n python-presage
Summary:	Python bindings for the predictive text entry system library
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Requires:	python

%description -n python-presage
Python bindings for the predictive text entry system library

%package dbus
Summary:	D-Bus bindings for the predictive text entry system library
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}

%description dbus
D-Bus bindings for the predictive text entry system library

%package text2ngram
Summary:	Generate statistical n-gram data from text
Group:		System/Libraries

%description text2ngram
Generate statistical n-gram data from text

%package gprompter
Summary:	Gprompter application showcasing the predictive text entry system library
Group:		System/Libraries

%description gprompter
Gprompter application showcasing the predictive text entry system library

%prep
%autosetup -p1 -n %{name}-%{version}%{?beta:~beta}
2to3 -w apps/dbus/presage_dbus_python_demo.in apps/dbus/presage_dbus_service apps/dbus/presage_dbus_service.py
cat > apps/dbus/org.gnome.presage.service.in <<EOF
[D-BUS Service]
Name=org.gnome.presage.beta
Exec={bindir}/presage_dbus_service --start
User=root
EOF
%configure

%build
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libpresage.so.1*

%files -n %{devname}
%{_libdir}/libpresage.so
%{_includedir}/presage.h
%{_includedir}/presageCallback.h
%{_includedir}/presageException.h

%files
%{_datadir}/presage

%files text2ngram
%{_bindir}/text2ngram
%{_mandir}/man1/text2ngram.1*

%files gprompter
%{_datadir}/applications/gprompter.desktop
%{_datadir}/icons/hicolor/scalable/apps/gprompter.svg
%{_mandir}/man1/gprompter.1*
%{_mandir}/man1/presage_demo.1*
%{_mandir}/man1/presage_demo_text.1*
%{_mandir}/man1/presage_simulator.1*
%{_datadir}/pixmaps/gprompter.png
%{_datadir}/pixmaps/gprompter.xpm
%{_sysconfdir}/presage.xml
%{_bindir}/gpresagemate
%{_bindir}/gprompter
%{_bindir}/presage_demo
%{_bindir}/presage_demo_text
%{_bindir}/presage_simulator

%files -n python-presage
%{_prefix}/lib/python*/site-packages/__pycache__/*
%{_prefix}/lib/python*/site-packages/presage_dbus_service.py

%files dbus
%{_bindir}/presage_dbus_python_demo
%{_bindir}/presage_dbus_service
%{_datadir}/dbus-1/services/org.gnome.presage.service
%{_mandir}/man1/presage_dbus_python_demo.1*
%{_mandir}/man1/presage_dbus_service.1*
