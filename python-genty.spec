#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Running a test with multiple data sets
Summary(pl.UTF-8):	Uruchamianie testu z wieloma zbiorami danych
Name:		python-genty
Version:	1.3.2
Release:	5
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/genty/
Source0:	https://files.pythonhosted.org/packages/source/g/genty/genty-%{version}.tar.gz
# Source0-md5:	45141bfcd0b77ff8e52e5de2944ff157
Patch0:		%{name}-mock.patch
URL:		https://pypi.org/project/genty/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mock
BuildRequires:	python-six
%if "%{py_ver}" < "2.7"
BuildRequires:	python-ordereddict
BuildRequires:	python-unittest2
%endif
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Genty, pronounced "gen-tee", stands for "generate tests". It promotes
generative testing, where a single test can execute over a variety of
input.

%description -l pl.UTF-8
Genty, wymawiane jak "gen-tee", oznacza generowanie testów. Wspiera
testowanie generyczne, w którym pojedynczy test może być wykonywany na
wielu różnych wejściach.

%package -n python3-genty
Summary:	Running a test with multiple data sets
Summary(pl.UTF-8):	Uruchamianie testu z wieloma zbiorami danych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-genty
Genty, pronounced "gen-tee", stands for "generate tests". It promotes
generative testing, where a single test can execute over a variety of
input.

%description -n python3-genty -l pl.UTF-8
Genty, wymawiane jak "gen-tee", oznacza generowanie testów. Wspiera
testowanie generyczne, w którym pojedynczy test może być wykonywany na
wielu różnych wejściach.

%prep
%setup -q -n genty-%{version}
%patch -P 0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s test
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/genty
%{py_sitescriptdir}/genty-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-genty
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/genty
%{py3_sitescriptdir}/genty-%{version}-py*.egg-info
%endif
