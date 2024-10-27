<script setup lang="ts"></script>

<template>
  <div id="inicio" class="px-6 pt-14 lg:px-8">
    <div class="mx-auto max-w-2xl pt-24 text-center sm:pt-40">
      <h1 class="text-5xl font-semibold tracking-tight text-white sm:text-7xl">
        Detección de ataques <span class="text-hacker-green-soft">DDoS</span>
      </h1>
      <p
        class="mt-8 text-pretty text-lg font-medium text-zinc-200 sm:text-xl/8"
      >
        Comprender y estudiar este tipo de ataque cibernético es fundamental
        para prevenir y mitigar sus efectos, en especial en infraestructura
        crítica, como la de salud, energética, financiera y de
        telecomunicaciones.
      </p>
    </div>
  </div>

  <!-- Content section -->
  <div class="mx-auto mt-20 max-w-7xl px-6 lg:px-8">
    <div class="mx-auto max-w-2xl lg:mx-0 lg:max-w-none">
      <dl
        class="mt-16 grid grid-cols-1 gap-x-8 gap-y-12 sm:mt-20 sm:grid-cols-2 sm:gap-y-16 lg:mt-28 lg:grid-cols-4"
      >
        <div
          class="flex flex-col-reverse gap-y-3 border-l border-white/20 pl-6"
        >
          <dt class="text-base/7 text-zinc-300">
            Ataques DDoS Mitigados hasta ahora
          </dt>
          <dd class="text-3xl font-semibold tracking-tight text-white">
            10,2 M
          </dd>
        </div>
        <div
          class="flex flex-col-reverse gap-y-3 border-l border-white/20 pl-6"
        >
          <dt class="text-base/7 text-zinc-300">
            De datos asociados a tráfico DDoS malicioso
          </dt>
          <dd class="text-3xl font-semibold tracking-tight text-white">
            57 PB
          </dd>
        </div>
        <div
          class="flex flex-col-reverse gap-y-3 border-l border-white/20 pl-6"
        >
          <dt class="text-base/7 text-zinc-300">
            País que ha efectuado más ataques
          </dt>
          <dd class="text-3xl font-semibold tracking-tight text-white">
            <span class="fi fi-ar fis" /> Argentina
          </dd>
        </div>
        <div
          class="flex flex-col-reverse gap-y-3 border-l border-white/20 pl-6"
        >
          <dt class="text-base/7 text-zinc-300">
            Aumento en ataques DDoS respecto a 2023
          </dt>
          <dd class="text-3xl font-semibold tracking-tight text-white">30%</dd>
        </div>
      </dl>
      <div class="mt-12 mb-8">
        <p class="w-full text-sm font-light text-zinc-200">
          <span class="font-bold">Fuente: </span>
          <a
            href="https://blog.cloudflare.com/ddos-threat-report-for-2024-q2/"
            target="_blank"
            class="hover:text-hacker-green-soft"
            >DDoS threat report for 2024 Q2 - Cloudflare
          </a>
        </p>
      </div>
      <div
        class="mx-auto py-8 grid max-w-xl grid-cols-1 gap-8 text-base/7 text-zinc-300 lg:max-w-none"
      >
        <div>
          <p>
            Un ataque DDoS
            <span class="font-bold text-zinc-100"
              >(Denegación de Servicio Distribuida)</span
            >
            es como un <i>asalto masivo a un servidor</i>, donde múltiples
            dispositivos envían una avalancha de solicitudes que lo sobrecargan.
            <span class="font-extrabold text-zinc-200">El resultado: </span
            ><span class="font-medium"
              >Servicios caídos, usuarios frustrados y pérdidas económicas para
              las empresas afectadas.</span
            >
            Además, estos ataques pueden dañar la reputación y exponer
            vulnerabilidades adicionales.
          </p>
          <p class="mt-8">
            Afortunadamente, el
            <span class="font-extrabold text-zinc-100"
              >Machine Learning y el Deep Learning</span
            >
            están dando una mano poderosa en la lucha contra los DDoS. Estos
            inteligentes algoritmos monitorean el tráfico en tiempo real,
            identificando y bloqueando patrones sospechosos al instante. Gracias
            a su capacidad de aprender y adaptarse, mejoran continuamente la
            defensa, haciendo que las redes sean más seguras y resistentes
            frente a las amenazas modernas.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
