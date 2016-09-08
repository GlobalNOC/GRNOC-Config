Name: perl-GRNOC-Config
Version: 1.0.9
Release: 1%{?dist}
Summary: GRNOC Config Library
License: CHECK(Distributable)
Group: Development/Libraries
URL: http://globalnoc.iu.edu
Source0: GRNOC-Config-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: perl >= 5.8.8
Requires: perl-XML-Simple 
Requires: perl-XML-XPath 
BuildRequires: perl-Test-Simple
BuildRequires: perl-Test-Pod
BuildRequires: perl-Test-Pod-Coverage

%description
GlobalNOC Config Library

%prep
%setup -q -n GRNOC-Config-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -p %{buildroot}/%{perl_sitelib}/GRNOC/
%{__install} lib/GRNOC/Config.pm %{buildroot}/%{perl_sitelib}/GRNOC/Config.pm
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%check
perl Makefile.PL
make test

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(644,root,root,-)
%{perl_sitelib}/GRNOC/Config.pm

