Summary:	Implementation of the SRS specification
Summary(pl):	Implementacja specyfikacji SRS
Name:		libsrs_alt
Version:	0.3
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://srs.mirtol.com/%{name}-%{version}.tar.gz
# Source0-md5:	8194b0468fb0d06e645780196b142df5
Patch0:		%{name}-am_ac.patch
URL:		http://srs.mirtol.com/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libspf-alt is an implementation of the SRS specification as found at
http://spf.pobox.com/srs.html.

%description -l pl
Libspf-alt jest implementacj± specyfikacji SRS, która znajduje siê pod
adresem http://spf.pobox.com/srs.html.

%package devel
Summary:	Header files for libsrs_alt library
Summary(pl):	Pliki nag³ówkowe biblioteki libsrs_alt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libsrs_alt library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libsrs_alt.

%package static
Summary:	Static libsrs_alt library
Summary(pl):	Statyczna biblioteka libsrs_alt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsrs_alt library.

%description static -l pl
Statyczna biblioteka libsrs_alt.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
