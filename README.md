# 3D Solar System in THREE.js

Welcome to the **3D Solar System** project, a dynamic and interactive simulation of our solar system created using THREE.js and the Vite framework.  
This project showcases advanced features and effects to provide an immersive experience of the celestial bodies in our solar system.  

Originally created by [Karol Fryc (N3rson)](https://github.com/N3rson/Solar-System-3D) and modified by [Blessy Sharon](https://github.com/blessyshrnxm).

---

![Solar_System](images/solar_system.png)  
![Earth](images/earthnew.png)  
![Mercury](images/mercury.png)  
![Mars](images/mars.png)  

---

## Features

### Standard Setup
- **Scene, Camera, Renderer**: Core setup for rendering 3D scenes.
- **Controls**: Interactive navigation.
- **Texture Loaders**: Efficient loading of planet/moon textures.

### Postprocessing Effects
- **BloomPass**: Adds a glowing effect to the Sun.
- **OutlinePass**: Highlights planets when hovered.
- **EffectComposer**: Combines and manages postprocessing effects.

### Star Background
- Realistic starry sky backdrop.

### Interactive Controls
- **dat.GUI**: Adjust orbit speed and Sun glow intensity.

### Lighting
- **AmbientLight**: Soft, global illumination.
- **PointLight**: Sunlight casting realistic shadows.

### Detailed Planet Creation
- **Attributes**: Size, tilt, texture, bump maps, rings, atmospheres.
- **Moons**: With realistic textures and orbits.
- **Earth Shader**: Day/night transitions and clouds.
- **Non-Spherical Moons**: Phobos & Deimos from 3D models.

### Realistic Orbits and Rotations
- Accurate orbital motion and axial rotation.
- Scaled sizes for visual balance.

### Shadows
- Realistic shadows from Sun’s PointLight.

### Asteroid Belts
- **Procedurally Generated**:  
  - 1000 asteroids (between Mars & Jupiter).  
  - 3000 asteroids (Kuiper belt).  
- **Performance Optimized**.

### Select Feature
- Hover outlines planets.
- Zoom in for details on click.
- Zoom out on close.

---

## Resources

Textures and 3D assets from:
- [NASA 3D Resources](https://nasa3d.arc.nasa.gov/images)  
- [Solar System Scope Textures](https://www.solarsystemscope.com/textures/)  
- [Planet Pixel Emporium](https://planetpixelemporium.com/index.php)  
- [TurboSquid](https://www.turbosquid.com/)  

---

## Installation and Setup

```sh
# 1. Clone the repository
git clone https://github.com/blessyshrnxm/solar-system-3d.git

# 2. Navigate into the project folder
cd solar-system-3d

# 3. Install dependencies
npm install

# 4. Start the dev server
npm run dev
