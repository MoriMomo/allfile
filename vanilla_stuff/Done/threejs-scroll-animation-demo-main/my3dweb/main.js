import './style.css'

import * as THREE from 'three';

import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'

const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

const renderer = new THREE.WebGLRenderer({
  canvas: document.querySelector('#bg'),
});

renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight);
camera.position.setZ(30);



renderer.render(scene, camera);
// ya yang ngerun animasi and stuff

const geometry = new THREE.TorusGeometry(10, 3, 16, 50)
const material = new THREE.MeshStandardMaterial({ color: 0xFF6347 })
const torus = new THREE.Mesh(geometry, material)

scene.add(torus)
// cicin yang muter di backgorund


const pointLight = new THREE.PointLight(0xFFFFFF)
pointLight.position.set(5, 5, 5)

const ambientLight = new THREE.AmbientLight(0xFFFFFF)

const lightHelper = new THREE.PointLightHelper(pointLight)

const GridHelper = new THREE.GridHelper(200, 50)

const controls = new OrbitControls(camera, renderer.domElement)
// dom elmeement itu event yang ada di mouse kayak di scroll di klik gitu dah
function addStar() {
  const geometry = new THREE.SphereGeometry(0.25, 24, 24)
  const material = new THREE.MeshStandardMaterial({ color: 0xffffff })
  const star = new THREE.Mesh(geometry, material);

  const [x, y, z] = Array(3).fill().map(() => THREE.MathUtils.randFloatSpread(100))
  star.position.set(x, y, z);
  scene.add(star)
}
Array(200).fill().forEach(addStar)

const spaceTexture = new THREE.TextureLoader().load('sapce.jpg')
scene.background = spaceTexture;
//troll box
const trollTexture = new THREE.TextureLoader().load('trollface.png')
const troll = new THREE.Mesh(
  new THREE.BoxGeometry(3, 3, 3),
  new THREE.MeshBasicMaterial({ map: trollTexture })
);
scene.add(troll)

// obama
const obamaTexture = new THREE.TextureLoader().load('obama spehere.jpg');
const obama = new THREE.Mesh(
  new THREE.SphereGeometry(3, 32, 32),
  new THREE.MeshStandardMaterial({ map: obamaTexture })
);
scene.add(obama)
scene.add(pointLight, ambientLight);
scene.add(lightHelper, GridHelper)

obama.position.z = 30;
obama.position.setX(-10);

troll.position.z = -5;
troll.position.x = 2;

function moveCamera() {
  const t = document.body.getBoundingClientRect().top;
  obama.rotation.z += 0.05;
  obama.rotation.y += 0.075;
  obama.rotation.x += 0.05;

  troll.rotation.y += 0.01;
  troll.rotation.z += 0.01;

  camera.position.z = t * -0.01;
  camera.position.x = t * -0.0002;
  camera.rotation.y = t * -0.0002;

}
document.body.onscroll = moveCamera
moveCamera()

function animate() {
  requestAnimationFrame(animate);

  torus.rotation.x += 0.01;
  torus.rotation.y += 0.005;
  torus.rotation.z += 0.01;

  obama.rotation.x += 0.005;
  renderer.render(scene, camera);
}
animate()

//setiap kita buat sesuatu kita harus render pake renderer.render(scene, camera)
//tapi dari pada di tulis ulang mulu mending pake function yang selalu ngerender kalau ngesave