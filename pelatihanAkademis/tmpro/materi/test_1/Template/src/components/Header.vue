<template>
  <header class="header">
    <div class="container">
      <div class="row">
        <div class="col-lg-6">
          <div class="header__logo">
            <router-link tag="a" to="/">
              <img src="../assets/logo.png" alt="" />
            </router-link>
          </div>
        </div>
        <div class="col-lg-6">
          <nav class="header__menu">
            <ul>
              <li>
                <router-link tag="a" to="/NewMovie">
                  Add New Movie
                </router-link>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </div>
  </header>
</template>

<style>
/*---------------------
  Header
-----------------------*/
.header__logo {
  padding: 15px 0;
}

.header__logo img {
  width: 200px;
  padding-top: 10px;
}

.header__logo a {
  display: inline-block;
}

.header__menu {
  padding: 24px 0;
}

.header__menu ul li {
  list-style: none;
  margin-right: 50px;
  position: relative;
  text-align: right;
}

.header__menu ul li:hover > a {
  color: #7fad39;
}

.header__menu ul li:last-child {
  margin-right: 0;
}

.header__menu ul li a {
  font-size: 14px;
  color: #252525;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 2px;
  transition: all, 0.3s;
  padding: 5px 0;
  display: block;
}
</style>