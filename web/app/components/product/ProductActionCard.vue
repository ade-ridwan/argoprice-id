<script setup lang="ts">
import { ref, computed } from 'vue';

const props = defineProps<{
  priceString: string;
  unit: string;
  stock: number;
}>();

const quantity = ref(1);

const parsePrice = (priceStr: string) => {
  return parseInt(priceStr.replace(/\D/g, '')) || 0;
};

const subtotal = computed(() => {
  return parsePrice(props.priceString) * quantity.value;
});

const increase = () => {
  if (quantity.value < props.stock) quantity.value++;
};

const decrease = () => {
  if (quantity.value > 1) quantity.value--;
};
</script>

<template>
  <div class="bg-white dark:bg-zinc-950 border border-gray-200 dark:border-zinc-800 rounded-2xl p-5 sm:p-6 shadow-sm sticky top-24">
    <h3 class="font-bold text-lg text-gray-900 dark:text-zinc-100 mb-4">Set Quantity</h3>
    
    <div class="flex items-center gap-4 mb-6">
      <div class="flex items-center border border-gray-300 dark:border-zinc-700 rounded-lg overflow-hidden h-10 w-32">
        <button 
          @click="decrease"
          class="w-10 h-full flex items-center justify-center text-gray-500 hover:bg-gray-100 dark:hover:bg-zinc-800 transition-colors disabled:opacity-50"
          :disabled="quantity <= 1"
        >
          <Icon name="lucide:minus" class="w-4 h-4" />
        </button>
        <div class="flex-1 h-full flex items-center justify-center font-medium text-gray-900 dark:text-zinc-100 border-x border-gray-300 dark:border-zinc-700">
          {{ quantity }}
        </div>
        <button 
          @click="increase"
          class="w-10 h-full flex items-center justify-center text-[#1A7B44] hover:bg-[#1A7B44]/10 transition-colors disabled:opacity-50"
          :disabled="quantity >= stock"
        >
          <Icon name="lucide:plus" class="w-4 h-4" />
        </button>
      </div>
      <div class="text-sm text-gray-500 dark:text-zinc-400">
        Stock: <span class="font-bold text-gray-900 dark:text-zinc-100">{{ stock }}</span> {{ unit }}
      </div>
    </div>

    <div class="flex items-center justify-between py-4 border-t border-gray-200 dark:border-zinc-800 mb-6">
      <span class="text-gray-600 dark:text-zinc-400 font-medium">Subtotal</span>
      <span class="text-xl font-bold text-gray-900 dark:text-zinc-100">Rp {{ subtotal.toLocaleString('id-ID') }}</span>
    </div>

    <div class="flex flex-col gap-3">
      <button class="w-full bg-[#1A7B44] hover:bg-[#156638] text-white font-medium rounded-xl py-3 transition-colors shadow-sm flex items-center justify-center gap-2">
        <Icon name="lucide:shopping-bag" class="w-5 h-5" />
        Buy Now
      </button>
      <button class="w-full bg-white dark:bg-zinc-900 text-[#1A7B44] border border-[#1A7B44] hover:bg-[#1A7B44]/5 font-medium rounded-xl py-3 transition-colors flex items-center justify-center gap-2">
        <Icon name="lucide:plus" class="w-5 h-5" />
        Add to Cart
      </button>
    </div>

    <div class="mt-4 flex items-center justify-center gap-2 text-xs text-gray-500 dark:text-zinc-400">
      <Icon name="lucide:shield-check" class="w-4 h-4 text-[#1A7B44]" />
      Secure transaction guaranteed
    </div>
  </div>
</template>
