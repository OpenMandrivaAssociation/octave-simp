%define	pkgname simp

Summary:	Basic interval operations for Octave
Name:       octave-%{pkgname}
Version:	1.1.0
Release:       3
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/simp/
Conflicts:	octave-forge <= 20090607
Requires:	octave
BuildRequires:  octave-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildArch:	noarch

%description
This package defines basic operations on intervals for Octave.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .
mv %{pkgname}-%{version}/doc/*.pdf .

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%doc COPYING DESCRIPTION *.pdf
%{_datadir}/octave/packages/%{pkgname}-%{version}
