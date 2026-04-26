<script setup lang="ts">
import { reactive, ref } from 'vue';
import Input from '~/components/ui/input/Input.vue';
import Label from '~/components/ui/label/Label.vue';

definePageMeta({
    layout: 'auth'
})

const form = reactive({
    email: '',
    password: ''
})

const showPassword = ref(false)

const login = async () => {
    console.log("login payload:", form)
    // TODO: Implement API call here
}
</script>

<template>
    <div class="flex flex-col max-w-[440px] justify-center w-full">
        <!-- Logo Section -->
        <div class="flex items-center gap-2 mb-8">
            <NuxtLink to="/" class="flex justify-center mx-auto items-center gap-2">
                <AppLogo />
            </NuxtLink>
        </div>

        <!-- Container -->
        <div
            class="w-full bg-white dark:bg-zinc-950 sm:border sm:border-gray-200 dark:border-zinc-800 sm:rounded-xl sm:p-8 sm:shadow-sm">
            <div class="mb-5">
                <h1 class="text-xl font-bold text-gray-900 dark:text-zinc-100 mb-1">Login Akun</h1>
                <p class="text-sm text-gray-500 dark:text-zinc-400">
                    Hi, Selamat Datang <span class="text-[#1A7B44] font-medium">#KomoditiKita</span>
                </p>
            </div>

            <form class="space-y-4" @submit.prevent="login">
                <!-- Email -->
                <div class="space-y-1.5">
                    <Label class="text-[13px] font-semibold text-gray-700 dark:text-zinc-300">Email</Label>
                    <Input 
                        v-model="form.email" type="email" placeholder="Masukkan email kamu"
                        class="h-10 text-sm rounded-lg border-gray-200 dark:border-zinc-800 dark:bg-zinc-900 dark:text-zinc-100 focus-visible:ring-[#1A7B44]/20 focus-visible:border-[#1A7B44]" />
                </div>

                <!-- Password -->
                <div class="space-y-1.5">
                    <Label class="text-[13px] font-semibold text-gray-700 dark:text-zinc-300">Password</Label>
                    <div class="relative">
                        <Input 
                            v-model="form.password"
                            :type="showPassword ? 'text' : 'password'"
                            placeholder="Masukkan password kamu"
                            class="h-10 text-sm pr-10 rounded-lg border-gray-200 dark:border-zinc-800 dark:bg-zinc-900 dark:text-zinc-100 focus-visible:ring-[#1A7B44]/20 focus-visible:border-[#1A7B44]" />
                        <button 
                            type="button"
                            class="absolute right-3 top-2.5 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors focus:outline-none"
                            @click="showPassword = !showPassword">
                            <Icon :name="showPassword ? 'lucide:eye-off' : 'lucide:eye'" class="h-[18px] w-[18px]" />
                        </button>
                    </div>
                </div>

                <!-- Forgot Password Link -->
                <div class="flex justify-end pt-1">
                    <NuxtLink 
                        to="/forgot-password"
                        class="text-[12px] text-gray-500 dark:text-zinc-400 hover:text-[#1A7B44] dark:hover:text-[#1A7B44] transition-colors">
                        Lupa Kata sandi ?
                    </NuxtLink>
                </div>

                <!-- Submit Button -->
                <div class="pt-2">
                    <button 
                        type="submit"
                        class="w-full bg-[#1A7B44] hover:bg-[#156638] text-white font-medium rounded-lg py-2.5 text-[15px] transition-all duration-200 shadow-sm hover:shadow focus:outline-none focus:ring-2 focus:ring-[#1A7B44]/50 focus:ring-offset-2 active:scale-[0.98]">
                        Login
                    </button>
                </div>

                <!-- Register Link -->
                <div class="text-center pt-2">
                    <p class="text-[13px] text-gray-500 dark:text-zinc-400">
                        Belum punya akun ?
                        <NuxtLink to="/register" class="text-[#1A7B44] font-semibold hover:underline">Registrasi disini
                        </NuxtLink>
                    </p>
                </div>
            </form>
        </div>
    </div>
</template>
