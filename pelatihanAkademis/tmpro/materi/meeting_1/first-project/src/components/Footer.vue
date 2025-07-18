<template>
  <div>
    <div class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-data">
            <h1>TIK.ET</h1>
            <p>
              Best App For Movie Lovers In Indonesia! Movie Entertainment
              Platform From Cinema To Online Movie Streaming Selections.
            </p>
          </div>
          <div class="footer-data">
            <ul type="none">
              <li><a href="#">HOME</a></li>
              <li><a href="#">NEWS</a></li>
              <li><a href="#">CAREERS</a></li>
              <li><a href="#">CONTACT US</a></li>
              <li><a href="#">PRIVACY POLICY</a></li>
              <li><a href="#">TERMS & CONDITIONS</a></li>
            </ul>
          </div>
          <div class="footer-data">
            <div class="footer-socials-text">
              <p>TIK.ET SUPPORT</p>
              <p class="info-email">E-MAIL : HELP@TIK.ET</p>
            </div>
            <ul type="none" class="footer-socials">
              <li>
                <a href="#">
                  <i class="fa-brands fa-square-instagram"></i>
                </a>
              </li>
              <li>
                <a href="#">
                  <i class="fa-brands fa-youtube"></i>
                </a>
              </li>
              <li>
                <a href="#">
                  <i class="fa-brands fa-facebook-f"></i>
                </a>
              </li>
              <li>
                <a href="#">
                  <i class="fa-brands fa-twitter"></i>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="footer-copyright">
        <p>2022 TIK.ET - PT MOVIE TIKET. ALL RIGHTS RESERVED.</p>
      </div>
    </div>
  </div>
</template>

<style>
.footer-copyright {
  padding-top: 8px;
  padding-bottom: 5px;
  background-color: #04009a;
}

.footer-copyright p {
  padding-bottom: 10px;
  margin-bottom: 0px;
  text-align: center;
}

.footer {
  background-color: #03045e;
  margin-bottom: 0px;
}

.footer,
.footer ul li a {
  color: white;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  padding-top: 10px;
  padding-bottom: 10px;
}

.footer-content .footer-data {
  width: 30%;
}

.footer-data ul li {
  padding-top: 2px;
  padding-bottom: 2px;
}

.footer-socials {
  display: flex;
  justify-content: flex-start;
  padding: 20px;
}

.footer-socials li {
  margin-right: 20px;
}

.footer-socials-text {
  padding: 20px;
}

.footer-socials-text p {
  margin-top: 0px;
  margin-bottom: 0px;
}

.info-email {
  font-size: 13px;
}
</style>