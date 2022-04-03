%define octpkg simp

Summary:	Basic interval operations for Octave
Name:		octave-%{octpkg}
Version:	1.1.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel > 3.8.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
This package define the basic operations on intervals for Octave.
It is useful when some values for a computation are incerte.

This package is part of unmantained Octave-Forge collection.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild
