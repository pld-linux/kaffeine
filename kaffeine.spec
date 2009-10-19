# TODO
# - kaffeine-mozilla-0.2.tar.bz2 (Starter-Plugin for Mozilla)
# - check: http://kaffeine.sourceforge.net/index.php?page=faq#question4

%define		qt_ver	4.4
%define		subver	pre2
%define		rel		1
Summary:	Full featured Multimedia-Player for KDE
Summary(pl.UTF-8):	Frontend do xine pod KDE
Name:		kaffeine
Version:	1.0
Release:	0.%{subver}.%{rel}
License:	GPL v2+
Group:		X11/Applications/Multimedia
# get it via: svn co svn://anonsvn.kde.org/home/kde/trunk/extragear/multimedia/kaffeine
Source0:	http://dl.sourceforge.net/project/kaffeine/kaffeine/%{name}-%{version}-%{subver}/kaffeine-%{version}-%{subver}.tar.gz
# Source0-md5:	24eee004427d6b3f73ffb85a94fc6e3b
URL:		http://kaffeine.kde.org/
BuildRequires:	kde4-kdelibs-devel >= 4.2
BuildRequires:	phonon-devel >= 4.3
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.122
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kaffeine is a full featured Multimedia-Player for KDE. By default it
uses xine as backend.

%description -l pl.UTF-8
W pełni zintegrowany z KDE frontend do xine.

%prep
%setup -q -n %{name}-%{version}-%{subver}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/x-test

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaffeine
%{_libdir}/kde4/kaffeinedvb.so
%{_datadir}/apps/kaffeine
%{_datadir}/apps/solid/actions/*.desktop
%{_desktopdir}/kde4/kaffeine.desktop
%{_iconsdir}/oxygen/*/actions/audio-radio-encrypted.png
%{_iconsdir}/oxygen/*/actions/video-television-encrypted.png
