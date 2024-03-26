%global debug_package %{nil} # Don't generate debug info
%define perl_lib /opt/grnoc/venv/
%define specfile_deps %(cat cpanfile | sed -r 's/^requires ([^[:space:]]*)/Requires: perl(\\1)/' | sed 's/["'"'"';]//g')
Name: perl-GRNOC-Config
Version: 1.0.10
Release: 1%{?dist}
Summary: GRNOC Config Library
License: CHECK(Distributable)
Group: Development/Libraries
URL: http://globalnoc.iu.edu
Source0: GRNOC-Config-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%if 0%{?rhel} == 8
BuildArch: x86_64
%else
BuildArch: noarch
%endif
Requires: perl >= 5.8.8
%if 0%{?rhel} == 7
%{specfile_deps}
%endif

%description
GlobalNOC Config Library

%prep
%setup -q -n GRNOC-Config-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -p %{buildroot}/%{perl_lib}/GRNOC/
%{__install} lib/GRNOC/Config.pm %{buildroot}/%{perl_lib}/GRNOC/Config.pm
%if 0%{rhel} == 8
%{__install} -d -p %{buildroot}%{perl_lib}%{name}/lib/perl5
cp -r venv/lib/perl5/* -t %{buildroot}%{perl_lib}%{name}/lib/perl5
%endif
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%check
perl Makefile.PL
make test

%clean
%{__rm} -rf %{buildroot}

%files
%if %{rhel} == 8
%{perl_lib}/%{name}/lib/perl5/*
%endif
%defattr(644,root,root,-)
%{perl_lib}/GRNOC/Config.pm

