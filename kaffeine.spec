
Summary:	A KDE xine frontend
Summary(pl):	Frontend do xine pod KDE
Name:		kaffeine
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	bdfae4914c81afa5236d0df3669f74cd
Patch0:		%{name}-no_doc_no_mime.patch
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	rpmbuild(macros) >= 1.122
BuildRequires:	xine-lib-devel >= 1:1.0
Requires:	kdebase-core >= 9:3.1.90
Requires:	xine-lib >= 1:1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A powerful, fully integrated with KDE xine GUI.

%description -l pl
W pe³ni zintegrowany z KDE frontend do xine.

%prep
%setup -q
%patch0 -p1

%build

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Multimedia/%{name}.desktop \
    $RPM_BUILD_ROOT%{_desktopdir}

echo "Categories=Qt;KDE;AudioVideo;" \
	>> $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaffeine
%{_libdir}/libkaffeinepart.la
%attr(755,root,root) %{_libdir}/libkaffeinepart.so
%{_datadir}/apps/kaffeine
%{_datadir}/apps/profiles/kaffeine.profile.xml
%{_datadir}/services/kaffeine_part.desktop
%{_desktopdir}/kaffeine.desktop
%{_iconsdir}/[!l]*/*/*/*.png
