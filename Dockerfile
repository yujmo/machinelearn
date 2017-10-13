FROM yujmo/archbase
RUN yaourt -S tk --noconfirm && yaourt -S python-pip --noconfirm && pip install numpy \
	&& pip install scipy && pip install scikit-learn && pip install matplotlib
