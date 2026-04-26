<script setup lang="ts">
import { reactive, ref } from 'vue';
import Input from '~/components/ui/input/Input.vue';
import Label from '~/components/ui/label/Label.vue';
import { REGISTER_URL } from '~/utils/constants';

definePageMeta({
    layout: 'auth'
})

interface RegisterForm {
    nama: string;
    email: string;
    provinsi: string;
    kota: string;
    password: string;
    password_confirmation: string;
}

const config = useRuntimeConfig()
const form = reactive<RegisterForm>({
    nama: '',
    email: '',
    provinsi: '',
    kota: '',
    password: '',
    password_confirmation: '',
})

const showPassword = ref(false)
const showConfirmPassword = ref(false)

const register = async () => {
    try {
        const payload = {
            username: form.nama,
            email: form.email,
            password: form.password,
            provinsi: form.provinsi,
            kota: form.kota,
            password_confirmation: form.password_confirmation
        };
        const res = await $fetch(`${config.public.apiBase}/${REGISTER_URL}`, {
            method: 'POST',
            body: payload
        });
        console.log("res: ", res);
    } catch (error) {
        console.log("error: ", error);
    }
}
</script>

<template>
    <!-- Container -->
    <div
        class="w-full max-w-[440px] bg-white dark:bg-zinc-950 sm:border sm:border-gray-200 dark:border-zinc-800 sm:rounded-2xl sm:p-8 sm:shadow-sm">
        <div class="mb-6">
            <h1 class="text-xl font-bold text-gray-900 dark:text-zinc-100 mb-1">Registrasi Akun</h1>
            <p class="text-sm text-gray-500 dark:text-zinc-400">
                Hi, Selamat Datang <span class="text-[#1A7B44] font-medium">#KomoditiKita</span>
            </p>
        </div>

        <form class="space-y-4" @submit.prevent="register">
            <!-- Nama -->
            <div class="space-y-1.5">
                <Label class="text-[13px] font-semibold text-gray-700 dark:text-zinc-300">Nama</Label>
                <Input 
                    v-model="form.nama" type="text" placeholder="Masukkan nama kamu"
                    class="h-10 text-sm rounded-lg border-gray-200 dark:border-zinc-800 dark:bg-zinc-900 dark:text-zinc-100 focus-visible:ring-[#1A7B44]/20 focus-visible:border-[#1A7B44]" />
            </div>

            <!-- Email -->
            <div class="space-y-1.5">
                <Label class="text-[13px] font-semibold text-gray-700 dark:text-zinc-300">Email</Label>
                <Input 
                    v-model="form.email" type="email" placeholder="Masukkan email kamu"
                    class="h-10 text-sm rounded-lg border-gray-200 dark:border-zinc-800 dark:bg-zinc-900 dark:text-zinc-100 focus-visible:ring-[#1A7B44]/20 focus-visible:border-[#1A7B44]" />
            </div>

            <!-- Provinsi -->
            <div class="space-y-1.5">
                <Label class="text-[13px] font-semibold text-gray-700 dark:text-zinc-300">Provinsi</Label>
                <div class="relative">
                    <select 
                        v-model="form.provinsi"
                        class="flex h-10 w-full items-center justify-between rounded-lg border border-gray-200 dark:border-zinc-800 bg-gray-50 dark:bg-zinc-900 px-3 py-2 text-sm text-gray-600 dark:text-zinc-100 shadow-sm ring-offset-background focus:outline-none focus:ring-2 focus:ring-[#1A7B44]/20 focus:border-[#1A7B44] disabled:cursor-not-allowed disabled:opacity-50 appearance-none transition-colors">
                        <option value="" disabled selected>Pilih</option>
                        <option value="jawa-barat">Jawa Barat</option>
                        <option value="jawa-tengah">Jawa Tengah</option>
                        <option value="jawa-timur">Jawa Timur</option>
                        <option value="banten">Banten</option>
                        <option value="dki-jakarta">DKI Jakarta</option>
                        <!-- Tambahkan provinsi lain sesuai kebutuhan -->
                    </select>
                    <Icon 
                        name="lucide:chevron-down"
                        class="absolute right-3 top-3 h-4 w-4 text-gray-400 pointer-events-none" />
                </div>
            </div>

            <!-- Kota -->
            <div class="space-y-1.5">
                <Label class="text-[13px] font-semibold text-gray-700 dark:text-zinc-300">Kota</Label>
                <div class="relative">
                    <select 
                        v-model="form.kota"
                        class="flex h-10 w-full items-center justify-between rounded-lg border border-gray-200 dark:border-zinc-800 bg-gray-50 dark:bg-zinc-900 px-3 py-2 text-sm text-gray-600 dark:text-zinc-100 shadow-sm ring-offset-background focus:outline-none focus:ring-2 focus:ring-[#1A7B44]/20 focus:border-[#1A7B44] disabled:cursor-not-allowed disabled:opacity-50 appearance-none transition-colors">
                        <option value="" disabled selected>Pilih</option>
                        <option value="bandung">Bandung</option>
                        <option value="semarang">Semarang</option>
                        <option value="surabaya">Surabaya</option>
                        <option value="jakarta">Jakarta</option>
                        <!-- Tambahkan kota lain sesuai kebutuhan -->
                    </select>
                    <Icon 
                        name="lucide:chevron-down"
                        class="absolute right-3 top-3 h-4 w-4 text-gray-400 pointer-events-none" />
                </div>
            </div>

            <!-- Password -->
            <div class="space-y-1.5">
                <div class="flex items-center gap-1">
                    <Label class="text-[13px] font-semibold text-gray-700 dark:text-zinc-300">Password</Label>
                    <span class="text-[11px] text-gray-400 font-normal">(minimal password 8 karakter)</span>
                </div>
                <div class="relative">
                    <Input 
                        v-model="form.password" :type="showPassword ? 'text' : 'password'"
                        placeholder="Masukkan password kamu"
                        class="h-10 text-sm pr-10 rounded-lg border-gray-200 dark:border-zinc-800 dark:bg-zinc-900 dark:text-zinc-100 focus-visible:ring-[#1A7B44]/20 focus-visible:border-[#1A7B44]" />
                    <button 
                        type="button" 
                        class="absolute right-3 top-2.5 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors focus:outline-none"
                        @click="showPassword = !showPassword">
                        <Icon 
                            :name="showPassword ? 'lucide:eye-off' : 'lucide:eye'"
                            class="h-[18px] w-[18px]" />
                    </button>
                </div>
            </div>

            <!-- Konfirmasi Password -->
            <div class="space-y-1.5">
                <Label class="text-[13px] font-semibold text-gray-700 dark:text-zinc-300">Konfirmasi
                    Password</Label>
                <div class="relative">
                    <Input 
                        v-model="form.password_confirmation"
                        :type="showConfirmPassword ? 'text' : 'password'"
                        placeholder="Masukkan konfirmasi password kamu"
                        class="h-10 text-sm pr-10 rounded-lg border-gray-200 dark:border-zinc-800 dark:bg-zinc-900 dark:text-zinc-100 focus-visible:ring-[#1A7B44]/20 focus-visible:border-[#1A7B44]" />
                    <button 
                        type="button" 
                        class="absolute right-3 top-2.5 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors focus:outline-none"
                        @click="showConfirmPassword = !showConfirmPassword">
                        <Icon 
                            :name="showConfirmPassword ? 'lucide:eye-off' : 'lucide:eye'"
                            class="h-[18px] w-[18px]" />
                    </button>
                </div>
            </div>

            <!-- Submit Button -->
            <div class="pt-4">
                <button
                    type="submit"
                    class="w-full bg-[#1A7B44] hover:bg-[#156638] text-white font-medium rounded-lg py-2.5 text-[15px] transition-all duration-200 shadow-sm hover:shadow focus:outline-none focus:ring-2 focus:ring-[#1A7B44]/50 focus:ring-offset-2 active:scale-[0.98]">
                    Registrasi
                </button>
            </div>

            <!-- Login Link -->
            <div class="text-center pt-2">
                <p class="text-[13px] text-gray-500 dark:text-zinc-400">
                    Sudah punya akun?
                    <NuxtLink to="/login" class="text-[#1A7B44] font-semibold hover:underline">Masuk disini
                    </NuxtLink>
                </p>
            </div>
        </form>
    </div>
</template>