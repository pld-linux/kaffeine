# TODO
# - check: http://kaffeine.sourceforge.net/index.php?page=faq#question4
%define		qt_ver	4.4
Summary:	Full featured Multimedia-Player for KDE
Summary(pl.UTF-8):	Frontend do xine pod KDE
Name:		kaffeine
Version:	1.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://downloads.sourceforge.net/project/kaffeine/kaffeine/%{name}-%{version}/kaffeine-%{version}.tar.gz
# Source0-md5:	72284197b1c90adf75149311e4422efe
URL:		http://kaffeine.kde.org/
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSvg-devel
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdelibs-devel >= 4.2
BuildRequires:	phonon-devel >= 4.3
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.577
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kaffeine is a full featured Multimedia-Player for KDE. By default it
uses xine as backend.

%description -l pl.UTF-8
W pełni zintegrowany z KDE frontend do xine.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaffeine
%attr(755,root,root) %{_bindir}/kaffeine-xbu
%{_datadir}/apps/profiles/kaffeine.profile.xml
%{_datadir}/apps/kaffeine
%{_datadir}/apps/solid/actions/*.desktop
%{_desktopdir}/kde4/kaffeine.desktop
%{_iconsdir}/oxygen/*/actions/audio-radio-encrypted.png
%{_iconsdir}/oxygen/*/actions/video-television-encrypted.png
