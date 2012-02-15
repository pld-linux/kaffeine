# TODO
# - check: http://kaffeine.sourceforge.net/index.php?page=faq#question4
%define		qtver	4.6.3
%define		kdever	4.5.1

Summary:	Full featured Multimedia-Player for KDE
Summary(pl.UTF-8):	Frontend do xine pod KDE
Name:		kaffeine
Version:	1.2.2
Release:	3
License:	GPL v2+
Group:		X11/Applications/Multimedia
#Source0:	http://downloads.sourceforge.net/project/kaffeine/kaffeine/%{name}-%{version}/kaffeine-%{version}.tar.gz
Source0:	http://downloads.sourceforge.net/project/kaffeine/current/kaffeine-%{version}.tar.gz
# Source0-md5:	690e48d2e5fe123887109aa9b1bc1c31
URL:		http://kaffeine.kde.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	phonon-devel >= 4.4.2
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.577
BuildRequires:	xine-lib-devel >= 1.1.0
BuildRequires:	xorg-lib-libXScrnSaver-devel
Requires:	QtSql-sqlite3
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
%cmake ../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT${_datadir}/locale/{sr@ijekavian,sr@ijekavianlatin}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaffeine
%attr(755,root,root) %{_bindir}/kaffeine-xbu
%{_datadir}/apps/profiles/kaffeine.profile.xml
%{_datadir}/apps/kaffeine
%{_datadir}/apps/solid/actions/*.desktop
%{_desktopdir}/kde4/kaffeine.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/kaffeine.svgz
%{_iconsdir}/oxygen/*/actions/audio-radio-encrypted.png
%{_iconsdir}/oxygen/*/actions/video-television-encrypted.png
