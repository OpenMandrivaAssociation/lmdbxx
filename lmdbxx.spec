	
Name: lmdbxx
Version: 1.0.0
Release: 2
License: Public Domain
Summary: C++ wrapper for the LMDB embedded B+ tree database library
URL: https://github.com/hoytech/lmdbxx
Source0 :https://github.com/hoytech/lmdbxx/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
 
BuildRequires: make
 
%description
Header-only %{summary}.
 
%package devel
Summary: Development files for %{name}
Requires: pkgconfig(lmdb)

 
%description devel
%{summary}.
 
%prep
%autosetup -p1
%build

%make_build
%install
%make_install PREFIX=%{_prefix}
 
%files devel
%doc README.md FUNCTIONS.rst AUTHORS CREDITS VERSION
%license UNLICENSE
%{_includedir}/lmdb++.h
