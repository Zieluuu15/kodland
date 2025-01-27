<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"
    />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="stylesheet" href="../static/css/style.css" />
    <title>Portfolio</title>
  </head>
  <body>
    <header class="header">
      <nav class="header__nav main-nav">
        <ul class="main-nav__list main-list">
          <li class="main-list__item list-item">
            <a class="list-item__link" href="#home">STRONA DOMOWA</a>
          </li>
          <li class="main-list__item list-item">
            <a class="list-item__link" href="#about">O MNIE</a>
          </li>
          <li class="main-list__item list-item">
            <a class="list-item__link" href="#skills">MOJE UMIEJĘTNOŚCI</a>
          </li>
        </ul>
      </nav>
    </header>
    <main class="main">
      <!-- Preview section -->
      <section class="main__home home" id="home">
        <h1 class="home__title">Szymon Zieliński</h1>
        <p class="home__subtitle">lubi szkołe</p>
      </section>
      <!-- About me section -->
      <section class="main__about about" id="about">
        <h2 class="about__title">O MNIE</h2>
        <div class="about__info info-block">
          <p class="info-block__text">
            Lubię szkołe, lubię się uczyć nowych rzeczy i lubię programować!
          </p>
          <img
            class="info-block__img"
            src="../static/img/profile.png"
            alt="me"
            width="250"
            height="250"
          />
        </div>
      </section>
      <!-- Sekcja umiejętności -->
      <section class="main__skills skills" id="skills">
        <h2 class="skills__title">MOJE UMIEJĘTNOŚCI</h2>
        <form action="/" method="POST">
          <ul class="skills__list skills-list">
            <li class="skills-list__skill skill">
              <img
                class="skill__img"
                src="../static/img/01.png"
                alt="python"
                width="150"
                height="150"
              />
              <span class="skill__info">Umiem grać w piłkę nożną i w szkole wygrywam ze składem!</span>
              <input class="skill__button" type="submit" name="button_python" value=" ...">
            </li>
            <li class="skills-list__skill skill">
              <img
                class="skill__img"
                src="../static/img/chicken.png"
                alt="discord"
                width="150"
                height="150"
              />
              <span class="skill__info">Dobrze się uczę w szkole</span>
              <input class="skill__button" type="submit" name="button_discord" value="...">
            </li>
            <li class="skills-list__skill skill">
              <img
                class="skill__img"
                src="../static/img/elephant.png"
                alt="html"
                width="150"
                height="150"
              />
              <span class="skill__info">Oglądam Youtube'a</span>
              <input class="skill__button" type="submit" name="button_html" value="...">
            </li>
            <li class="skills-list__skill skill">
              <img
                class="skill__img"
                src="../static/img/giraffe.png"
                alt="SQL"
                width="150"
                height="150"
              />
              <span class="skill__info">Odpoczywam, a potem mam siłę</span>
              <input class="skill__button" type="submit" name="button_db" value="...">
            </li>
          </ul>
        </form>
        {% if button_python%}
          <div class="skills__project project" id="project">
              <img class="project__img" src="../static/img/python-project.png" alt="project" width="500">
              <a class="project__link" href="">Otwórz w GitHub</a>
          </div>
        {% endif %}
      </section>
      <!-- Feedback form -->
      <section class="main__feedback feedback" id="feedback">
        <h2 class="feedback__title">Informacja zwrotna</h2>
        <form action="" method="POST" class="feedback__form form">
          <label for="email">
            <input type="email" class="form__input" name="email" id="email" placeholder="Podaj E-mail" required>
          </label>
          <label for="text">
            <textarea name="text" class="form__input" id="text" cols="70" rows="10" required placeholder="Comment"></textarea>
          </label>
          <button class="form__button" type="submit">WYŚLIJ</button>
        </form>
      </section>
    </main>
    <!-- Stopka linków do mediów społecznościowych -->
    <footer>

    </footer>
  </body>
</html>
