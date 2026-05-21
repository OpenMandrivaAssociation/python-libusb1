%define module libusb1

Name:		python-libusb1
Version:	3.4.0
Release:	1
Summary:	Pure-python wrapper for libusb-1.0
License:	LGPL-2.1-or-later
Group:		Development/Python
URL:		https://pypi.org/project/libusb1
Source0:	https://files.pythonhosted.org/packages/source/l/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	%{_lib}usb1.0_0

%description
Pure-python wrapper for libusb-1.0

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%license COPYING COPYING.LESSER
%{python_sitelib}/%{module}.py
%{python_sitelib}/usb1
%{python_sitelib}/%{module}-%{version}*.*-info
