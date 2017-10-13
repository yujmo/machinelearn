FROM yujmo/archbase
RUN yaourt -S python-pip --noconfirm &&	pip install numpy && pip install scipy && pip install matplotlib && pip install scikit-learn
