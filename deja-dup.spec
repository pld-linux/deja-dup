Summary:	Backup tool
Summary(pl.UTF-8):	Narzędzie do wykonywania kopii zapasowych
Name:		deja-dup
Version:	50.0
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://gitlab.gnome.org/World/deja-dup/-/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	83db617f2255c98ba4bd40adb45f72c9
URL:		https://gitlab.gnome.org/World/deja-dup
BuildRequires:	blueprint-compiler >= 0.14
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.80
BuildRequires:	gtk4-devel >= 4.18
BuildRequires:	itstool
BuildRequires:	json-glib-devel >= 1.2
BuildRequires:	libadwaita-devel >= 1.8
BuildRequires:	libsecret-devel >= 0.18.6
BuildRequires:	libsoup3-devel >= 3.0
BuildRequires:	meson >= 1.1
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(find_lang) >= 1.35
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	vala
BuildRequires:	vala-libsecret
BuildRequires:	yelp-tools >= 3.2.0
Requires(post,postun):	glib2 >= 1:2.80
Requires(post,postun):	gtk-update-icon-cache
Requires:	duplicity >= 2.1.0
Requires:	hicolor-icon-theme
Requires:	libfuse3
Requires:	rclone
Requires:	restic >= 0.17.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Deja Dup is a simple backup tool. It hides the complexity of doing
backups the 'right way' (encrypted, off-site, and regular) and uses
duplicity/restic as the backend.

%description -l pl.UTF-8
Deja Dup jest prostym narzędziem do wykonywania kopii zapasowych.
Ukrywa on złożoność prawidłowych kopii zapasowych (szyfrowanych, poza
komputerem i regularnych) i używa programu duplicity/restic jako
mechanizmu.

%prep
%setup -q

%build
%meson \
	-Dpackagekit=disabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS.md PACKAGING.md README.md
%license LICENSES/*
%attr(755,root,root) %{_bindir}/deja-dup
%dir %{_libdir}/deja-dup
%{_libdir}/deja-dup/*
%dir %{_libexecdir}/deja-dup
%{_libexecdir}/deja-dup/*
%{_datadir}/dbus-1/services/org.gnome.DejaDup.service
%{_datadir}/glib-2.0/schemas/org.gnome.DejaDup.gschema.xml
%{_datadir}/help/*
%{_datadir}/metainfo/org.gnome.DejaDup.metainfo.xml
%{_desktopdir}/org.gnome.DejaDup.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.DejaDup.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.DejaDup-symbolic.svg
%{_sysconfdir}/xdg/autostart/org.gnome.DejaDup.Monitor.desktop
%{_mandir}/man1/deja-dup.1*
