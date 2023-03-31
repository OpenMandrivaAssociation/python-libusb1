Name:		python-libusb1
Version:	3.0.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/l/libusb1/libusb1-%{version}.tar.gz
Summary:	Pure-python wrapper for libusb-1.0
URL:		https://pypi.org/project/libusb1/
License:	LGPLv2.1+
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Pure-python wrapper for libusb-1.0

%prep
%autosetup -p1 -n libusb1-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/libusb1.py
%{py_sitedir}/usb1
%{py_sitedir}/libusb1-*.*-info
