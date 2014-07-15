%define	pkgname simp

Summary:	Basic interval operations for Octave
Name:       octave-%{pkgname}
Version:	1.1.0
Release:	4
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/simp/
BuildRequires:  octave-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildArch:	noarch
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
This package defines basic operations on intervals for Octave.

%prep
%setup -q -c %{pkgname}-%{version}
cp %{SOURCE0} .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %{SOURCE0} 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .
mv %{pkgname}-%{version}/doc/*.pdf .

%clean

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%doc COPYING DESCRIPTION *.pdf
%{_datadir}/octave/packages/%{pkgname}-%{version}
