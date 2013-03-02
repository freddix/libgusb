Summary:	GObject wrapper for libusb1 library
Name:		libgusb
Version:	0.1.5
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
# Source0-md5:	a2c849079ba5bae6277383a80fb01d12
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libusbx-devel
BuildRequires:	pkg-config
BuildRequires:	udev-glib-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop. This makes it easy to
integrate low level USB transfers with your high-level application or
system daemon.

%package devel
Summary:	Header files for GUsb library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for GUsb library.

%package apidocs
Summary:	GUsb API documentation
Group:		Documentation

%description apidocs
API and internal documentation for GUsb library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libgusb.so.?
%attr(755,root,root) %{_libdir}/libgusb.so.*.*.*
%{_libdir}/girepository-1.0/GUsb-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgusb.so
%{_includedir}/gusb-1
%{_libdir}/libgusb.la
%{_datadir}/gir-1.0/GUsb-1.0.gir
%{_datadir}/vala/vapi/gusb.vapi
%{_pkgconfigdir}/gusb.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gusb

