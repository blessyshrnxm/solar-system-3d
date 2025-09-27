# 3D Solar System in THREE.js  

An interactive 3D simulation of the solar system built with **Three.js** and **Vite**, designed as part of a final-year AR/VR project.  

Originally forked from [Karol Fryc (N3rson)](https://github.com/N3rson/Solar-System-3D), this project was **extended and customized** by [Blessy Sharon](https://github.com/blessyshrnxm) with the following contributions:  

- Added **interactive planetary core exploration** (crust, mantle, core layers with details on click).  
- Designed **educational UI panels** to display planetary facts for students.  
- Integrated feedback from **college exhibition demo** to improve usability.  
- Led a **5-member team**, coordinating tasks and ensuring timely delivery.  
- Deployed live via Vercel for public access and testing.  

---

## Features  

### Core Setup  
- **Scene, Camera, Renderer** for dynamic 3D rendering.  
- **Orbit Controls** for smooth navigation.  
- **Texture Loaders** for planets and moons.  

### Custom Modifications  
- **Planetary Layer Interaction**: Click planets to view internal structures.  
- **Educational Information Panels**: Interactive UI to display facts and details.  
- **Optimized for Demonstration**: Tested and refined for an exhibition audience.  

### Visual & Performance Enhancements  
- **BloomPass and OutlinePass** for immersive glow and hover effects.  
- **Earth Shader** with day/night cycles and atmosphere.  
- **Asteroid Belts** (3,000+ objects) generated procedurally.  
- **PointLight + Shadows** for realistic illumination.  

---

## Tech Stack  
- **Three.js** (3D rendering)  
- **JavaScript, HTML5, CSS3**  
- **Vite** (bundler)  
- **Deployment**: Vercel  

---

## Live Demo  
[3D Solar System Simulation](https://solar-system-3d-arvr.vercel.app/)  

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
